list(APPEND examples
    main
)

# message(STATUS "Examples ----------------------")
foreach(app ${examples})
    add_executable(${app} ${app}.cpp)
    target_link_libraries(${app} ${PROJECT_NAME})
endforeach()