#include <vector>
#include <string>
#include <fstream>

#include "utils.hpp"

void load_data(std::vector<std::string>& strs){
    std::ifstream f("./../data/words_for_prefix_search.csv");

    if(!f.is_open())
        return;

    std::string word;

    while(std::getline(f, word))
        strs.push_back(word);
}