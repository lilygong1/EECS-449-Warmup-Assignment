walker interact {
    can return_message with `root entry {
        report {
            "response": "Hello, world!"
        };
    }
}

walker interact_with_body {
    has name: str;

    can return_message with `root entry {
        report {
            "response": "Hello, " + self.name + "!"
        };
    }
}

walker temperature_converter {
    has fahrenheit: float;

    can return_message with `root entry {
        celsius = (self.fahrenheit - 32) * 5.0/9.0;
        report {
            "response": "The temperature " + str(self.fahrenheit) + "F is " + str(celsius) + "C."
        };
    }
}


walker add {
    has a: int;
    has b: int;

    can return_message with `root entry {
        report {
            "response": "The sum of " + str(self.a) + " and " + str(self.b) + " is " + str(self.a + self.b) + "."
        };
    }
}