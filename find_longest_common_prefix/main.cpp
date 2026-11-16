#include <iostream>

#include "find_longest_common_prefix.hpp"
#include "utils.hpp"

int main(){
    int method_option;

    std::cout << "Introduce which finding method you want to use";
    std::cout << "\n\t1. Horizontally";
    std::cout << "\n\t2. Exit\n";

    std::cin >> method_option;

    std::vector<std::string> strs;

    load_data(strs);

    std::string prefix;

    switch(method_option){
        case 1:
            longest_common_prefix_horizontally_searched(strs, prefix);
            break;
        case 2:
            break;
        default:
            break;
    }

    std::cout << "El prefijo encontrado es: " << prefix << std::endl;
}