#include <vector>
#include <string>

#include "find_longest_common_prefix.hpp"

void longest_common_prefix_horizontally_searched(const std::vector<std::string>& strs, std::string& prefix){
    prefix = "";

    if(strs.empty())
        return;

    for(std::size_t letter_pos = 0; letter_pos < strs[0].size(); letter_pos++){
        prefix.push_back(strs[0][letter_pos]);
        for(std::size_t word_pos = 1; word_pos < strs.size(); word_pos++){
            if(strs[word_pos-1][letter_pos] != strs[word_pos][letter_pos]){
                prefix.pop_back();
                return;
            }
        }
    }
}