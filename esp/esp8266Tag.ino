#include <QueueList.h>
#include <Ticker.h>
#include <ESP8266WiFi.h>
#include <string>

const char* ssid = "OnePlus3";
const char* password = "Lm794613852";
//IPAddress ip(192, 168, 1, 100);
String tagID = "1234567";
String help;

Ticker timer;
int timeInSecs = 43000;
int numNetworks;

QueueList<String> queue;

// Create an instance of the server
// specify the port to listen on as an argument
WiFiServer server(80);


void incrementTime() {
  timeInSecs++;
  if(timeInSecs >= 86400) {
    timeInSecs = 0;
  }
}

void setup() {
  Serial.begin(115200);
  delay(10);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  IPAddress ip(192,168,0,12);   
  IPAddress gateway(192,168,0,10);   
  IPAddress subnet(255,255,255,0);   
  WiFi.config(ip, gateway, subnet);
  
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());

  // increment seconds every 1.0s
  timer.attach(1, incrementTime);
}

void formatScan(int networksFound) {
  String s = "";
  String temp = "";
  s += "<p>" + String(timeInSecs) + ":";
  for(int i = 0; i < networksFound; i++) {
    //Serial.println(String(WiFi.SSID(i)));
    if(WiFi.channel(i) == 2) {
      //Serial.println(String(WiFi.SSID(i)));
      if(WiFi.SSID(i) == "ESPap1") {
         //sprintf(temp, " ESPap1=%d ", WiFi.RSSI(i));
         temp = " ESPap1=" + String(WiFi.RSSI(i)) + " ";
         s += temp;
         temp = "";
      }
      else if(WiFi.SSID(i) == "ESPap2") {
         //sprintf(temp, " ESPap2=%d ", WiFi.RSSI(i));
         temp = " ESPap2=" + String(WiFi.RSSI(i)) + " ";
         s += temp;
         temp = "";
      }
      else if(WiFi.SSID(i) == "ESPap0") {
         //sprintf(temp, " ESPap3=%d ", WiFi.RSSI(i));
         temp = " ESPap0=" + String(WiFi.RSSI(i)) + " ";
         s += temp;
         temp = "";
      }
    }
  }
  s += "</p>\r\n";
  if(queue.count() >= 6) {
    //Serial.println("making room in queue, it has " + String(queue.count()) + " items");
    queue.pop();
  }
  queue.push(s);
  //Serial.println("Queue has " + String(queue.count()) + " items.");

  WiFi.scanDelete();
}

void loop() {
  help = "";
  
  //scan networks
  numNetworks = WiFi.scanNetworks();
  formatScan(numNetworks);
  
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
  
  // Read the first line of the request
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  
  // Match the request
  int val;
  if(req.indexOf("/setIP/") != -1) {
    // change the IP to this... might not be able to do this :(
  }
  else if(req.indexOf("/setTagID/") != -1) {
    // change the tag id.. kinda funky, but should work
    tagID = "";
    for(int i = req.indexOf("/setTagId/") + 15; i < req.indexOf("/setTagId/") + 15 + 7; i++) {
      tagID += req[i];
    }
  }
  else if(req.indexOf("/getTriang") != -1) {
    // get the triangulation values into a string
    // something like "Time=12:53:46 RSSI1=-40 RSSI2=-90 RSSI3=-100\nTime=12:53:50..."
    // Might be easier to have an array of a buffer.. or even a queue would be nice
    // Don't forget you can use String types to make your life easier
    while(!queue.isEmpty()) {
      help += queue.pop();
    }
  }
  else if(req.indexOf("/setTime/") != -1) {
    Serial.println("Gotta change dat time");
    for(int i = req.indexOf("/setTime/") + 9; i < req.indexOf("/setTime/") + 9 + 5; i++) {
      help += req[i];
    }
    timeInSecs = atoi(help.c_str());
  }
  
  client.flush();

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\n";

  s += "<p>" + tagID + "</p>\r\n";
  s += help;
  
  s += "</html>\n";

  // Send the response to the client
  client.print(s);
  delay(1);
  Serial.println("Client disonnected");

  // The client will actually be disconnected 
  // when the function returns and 'client' object is detroyed
}

