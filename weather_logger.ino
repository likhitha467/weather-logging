


#include <Wire.h>
#include <DHT.h>

// DS1621 configuration
#define DS1621_ADDRESS 0x48

// DHT11 configuration
#define DHT_PIN 2
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup()
{
    Serial.begin(9600);

    Wire.begin();
    dht.begin();

    delay(1000);

    // Start DS1621 temperature conversion
    Wire.beginTransmission(DS1621_ADDRESS);
    Wire.write(0xEE);
    Wire.endTransmission();

    Serial.println("ENVIRONMENTAL DATA LOGGER");
    Serial.println("=========================");
}

void loop()
{
    float dsTemperature = -999;

    // Read DS1621 temperature
    Wire.beginTransmission(DS1621_ADDRESS);
    Wire.write(0xAA);

    if (Wire.endTransmission() == 0)
    {
        Wire.requestFrom(DS1621_ADDRESS, 2);

        if (Wire.available() >= 2)
        {
            int8_t whole = Wire.read();
            byte fraction = Wire.read();

            dsTemperature = whole + ((fraction & 0x80) ? 0.5 : 0.0);
        }
    }

    // Read DHT11
    float dhtTemperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Display results
    Serial.println("-------------------------");

    if (dsTemperature != -999)
    {
        Serial.print("DS1621 Temperature: ");
        Serial.print(dsTemperature);
        Serial.println(" C");
    }
    else
    {
        Serial.println("DS1621: Sensor Error");
    }

    if (!isnan(dhtTemperature) && !isnan(humidity))
    {
        Serial.print("DHT11 Temperature: ");
        Serial.print(dhtTemperature);
        Serial.println(" C");

        Serial.print("Humidity: ");
        Serial.print(humidity);
        Serial.println(" %");
    }
    else
    {
        Serial.println("DHT11: Sensor Error");
    }

    delay(2000);
}
