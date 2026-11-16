cmake_minimum_required(VERSION 3.16)

project(find_longest_common_prefix LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(find_longest_common_prefix
    main.cpp
    find_longest_common_prefix.cpp
    utils.cpp
)

set_target_properties(find_longest_common_prefix
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

target_compile_options(find_longest_common_prefix
    PRIVATE
        $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic>
)
