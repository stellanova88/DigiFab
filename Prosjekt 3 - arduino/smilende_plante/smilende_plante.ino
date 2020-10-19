#include <Wire.h>   //For kommunikasjon over I2C 
#include <Adafruit_GFX.h>   //Bibliotek for enkel grafikk for display
#include <Adafruit_SSD1306.h> //Bibliotek for Oled displayet

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

 
const int AirValue = 657;   //Høyeste verdi i luft
const int WaterValue = 310;  //Laveste verdi i vann (Nesten hele sensoren må ned i vann)
int moisture = 0;

//Nivåer på silefjesene
//const int deadL = 0;      //Laveste nivå på tilstand    (x)(x)
//const int mad = 10;      //Sur   :(
//const int neutral = 20;   //middels :|
//const int happy = 30;     //Glad  :)
//const int deadH = 100;   //Høyeste verdi på tilstand    (x)(x)


void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); //initialize with the I2C addr 0x3C (128x64)
  display.clearDisplay();
}

void loop() {
moisture = analogRead(A0);  //Gir verdi input et variabelnavn
Serial.println(moisture);
moisture = map(moisture, AirValue, WaterValue, 0, 100);
delay(2000);

//-------------------------------------------------- Dør  x[ ---------------------------------
if(moisture <=20 || moisture >= 75)     //Hvis planten har lite eller for mye vann (0 eller 100)
{
//Skriver prosent oppe i høyre hjørne:
  display.setCursor(0,0);
  display.setTextSize(1);
  display.println("Prosent:");

//Viser fuktighet prosenten:  
  display.setCursor(0,10);  //oled display
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.println(moisture);

//Runde øyner:
  display.drawCircle (80,15,15, WHITE); // Sirkel til hode (x-akse, y-akse, diameter)
  display.drawCircle (75,14,4, WHITE); // Venstre øye
  display.drawCircle (85,14,4, WHITE); // Høyre øye
  display.drawPixel (75,14, WHITE); // venstre pupille
  display.drawPixel  (85,14, WHITE); //høyre pupille

//Døde øyner
//Venstre øye (X)
  display.drawPixel (74,13, WHITE); // x, venstre oppe
  display.drawPixel (76,13, WHITE); // x, høyre oppe
  display.drawPixel (74,15, WHITE); // x, venstre nede
  display.drawPixel (76,15, WHITE); // x, høyre nede

//Høyre øye (X)
  display.drawPixel (84,13, WHITE);
  display.drawPixel (86,13, WHITE);
  display.drawPixel (84,15, WHITE);
  display.drawPixel (86,15, WHITE);

//Sur munn  :(
  display.drawLine (68,7, 110,7, WHITE); // Har en fargefeil i de 7 øverste y-akse pikslene på displayet, så gav han en caps
  display.drawPixel (74,25, WHITE); //...
  display.drawPixel (87,25, WHITE); 
  display.drawPixel (75,24, WHITE); 
  display.drawPixel (86,24, WHITE);
  display.drawPixel (76,23, WHITE);
  display.drawPixel (85,23, WHITE);
  display.drawLine (77,22,84,22, WHITE); //Nedre linje av munn
  display.display ();

  delay(250);
  display.clearDisplay();
}
//---------------------------------------Sur :( --------------------------------------------
else if(moisture <=35 || moisture >= 70)     //Hvis planten har lite eller for mye vann
{
//Skriver prosent oppe i høyre hjørne:
  display.setCursor(0,0);
  display.setTextSize(1);
  display.println("Prosent:");

//Viser fuktighet prosenten:  
  display.setCursor(0,10);  //oled display
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.println(moisture);

//Runde øyner  00
  display.drawCircle (80,15,15, WHITE); // Sirkel til hode (x-akse, y-akse, diameter)
  display.drawCircle (75,14,4, WHITE); // Venstre øye
  display.drawCircle (85,14,4, WHITE); // Høyre øye
  display.drawPixel (75,14, WHITE); // venstre pupille
  display.drawPixel  (85,14, WHITE); //høyre pupille

//Sur Munn :(
  display.drawLine (68,7, 110,7, WHITE); // Har en fargefeil i de 7 øverste y-akse pikslene på displayet, så gav han en caps
  display.drawPixel (74,25, WHITE); //...
  display.drawPixel (87,25, WHITE); 
  display.drawPixel (75,24, WHITE); 
  display.drawPixel (86,24, WHITE);
  display.drawPixel (76,23, WHITE);
  display.drawPixel (85,23, WHITE);
  display.drawLine (77,22,84,22, WHITE); //Nedre linje av munn
  display.display ();

  delay(250);
  display.clearDisplay();
}

// ------------------------------Nøytral :) ----------------------------------------
else if(moisture > 35 && moisture < 45)     
{
  display.setCursor(0,0);   //pixel oppe til venstre på displayet
  display.setTextSize(1);   //Størrelse på teksten
  display.println("Prosent:");  //Skriv ut tekst  
  
  display.setCursor(0,10);  //oled display (X-aske, Y-akse)
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.println(moisture);

//Runde øyner  00 
  display.drawCircle (80,15,15, WHITE); // Sirkel til hode (x-akse, y-akse, diameter)
  display.drawCircle (75,14,4, WHITE); // Venstre øye
  display.drawCircle (85,14,4, WHITE); // Høyre øye
  display.drawPixel (75,14, WHITE); // venstre pupille
  display.drawPixel  (85,14, WHITE); //høyre pupille
 
//Smilemunn   :)
  display.drawLine (68,7, 110,7, WHITE); // Har en fargefeil i de 7 øverste y-akse pikslene på displayet, så gav han en caps
  display.drawLine (76,24,85,24, WHITE); //Munn tegnet som en linje
  display.display ();

  delay(250);
  display.clearDisplay();

  delay(250);
  display.clearDisplay();
} 

//------------------------------------ Glad :) ----------------------------------------------
else if(moisture >=45 && moisture < 70)  //Sensoren er fuktig
{
  display.setCursor(0,0);
  display.setTextSize(1);
  display.println("Prosent:");
  
  display.setCursor(0,10);  //oled display
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.println(moisture);


//Smileøyner  00
  display.drawCircle (80,15,15, WHITE); // Sirkel til hode (x-akse, y-akse, diameter)
  display.drawCircle (75,14,4, WHITE); // Venstre øye
  display.drawCircle (85,14,4, WHITE); // Høyre øye
  display.drawPixel (75,14, WHITE); // venstre pupille
  display.drawPixel  (85,14, WHITE); //høyre pupille

//Smilemunn   :)
  display.drawLine (68,7, 110,7, WHITE); // Har en fargefeil i de 7 øverste y-akse pikslene på displayet, så gav han en caps
  display.drawPixel (73,22, WHITE); // Venstre munn
  display.drawPixel (88,22, WHITE); // Høyre munn
  display.drawPixel (74,23, WHITE); //...
  display.drawPixel (87,23, WHITE); 
  display.drawPixel (75,24, WHITE); 
  display.drawPixel (86,24, WHITE);
  display.drawPixel (76,25, WHITE);
  display.drawPixel (85,25, WHITE);
  display.drawLine (77,26,84,26, WHITE); //Nedre linje av munn
  display.display ();

  delay(250);
  display.clearDisplay();
}  
}
