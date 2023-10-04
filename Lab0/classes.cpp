#include <iostream>
#include <string>

class Footwear {
public:
    Footwear(const std::string& brand, const std::string& model, int size, double price) {
        this->brand = brand;
        this->model = model;
        this->size = size;
        this->price = price;
    }

    void displayDetails() {
        std::cout << "Brand: " << brand << std::endl;
        std::cout << "Model: " << model << std::endl;
        std::cout << "Size: " << size << std::endl;
        std::cout << "Price: $" << price << std::endl;
    }

private:
    std::string brand;
    std::string model;
    int size;
    double price;
};

int main() {
    Footwear myShoes("Nike", "Air Max", 10, 129.99);

    std::cout << "Footwear Details:" << std::endl;
    myShoes.displayDetails();

    return 0;
}