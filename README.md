# Search Assistant
Search Assistant is a command-line Python application that allows users to perform web searches using various input methods. It provides a flexible and user-friendly way to search the web based on quoted text extraction, direct text input, or a list of search queries. Users can customize the search site for each query, making it a versatile tool for web searches.

## Application Overview:
This utility offers a command-line interface that lets users perform web searches using various input methods. Users can choose between the following functionalities:
- <b>Input Quoted Text and Extract Quoted Phrases</b>: Users can input a piece of text, and the utility will extract phrases enclosed within double quotation marks (e.g., "search phrase"). The extracted phrases are presented to the user for further action, such as searching on different websites.
- <b>Input Direct Text for Web Search</b>: Users can input a single text query for web search. The utility will prompt the user to select a search site (e.g., Google, YouTube, YouTube Music, or a custom URL) for the search query.
- <b>Input a List of Queries</b>: Users can input a list of search queries. The utility allows users to select a single search site for all queries in the list or choose a different site for each query.

## Functions:
The application is structured around several functions, each with specific functionality:
- <b>`search(query, site)`</b>: Opens a web browser and performs a search on the specified site with the given query.
- <b>`extract_quoted_words(text)`</b>: Extracts phrases enclosed within double quotation marks from the input text and returns them as a list.
- <b>`choose_site()`</b>: Displays a list of available search sites and prompts the user to choose one. It returns the index of the chosen site in the exist_sites list.
- <b>`choose_site_for_each_element(words)`</b>: Allows the user to choose a different search site for each element in a list of search queries.
- <b>`choose_site_for_all_elements(words)`</b>: Allows the user to choose a single search site for all elements in a list of search queries.
- <b>`edit_list(words)`</b>: Enables the user to edit the list of search queries. Users can add, remove, or modify elements in the list.
- <b>`check_list(words)`</b>: Prompts the user to confirm the list of search queries or edit it before proceeding to search.
- <b>`assistant(text, in_type, word)`</b>: Orchestrates the user interaction based on the selected input type (quoted text extraction, direct text input, or list input) and the list of search queries. It guides the user through the process of selecting a search method and site.
- <b>`interface()`</b>: The main user interface of the application. It allows users to choose the input type and provides a menu for entering text or lists.

## Prerequisites

- Python 3.x

## How to Use
- **First Way**
   - Download Search Assistant.exe

- **Second Way**
   - Clone this repository or download the script.
   - Open your terminal or command prompt on the directory of Search Assistant.py and run the following script:

      ```bash
     python Search Assistant.py
     ```

### Application Interface 
- [x] ***Choose what you want***
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/e0089afb-f4f2-4a3e-b8f8-97fb7d82841d)


***1***
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/f5ba938e-671a-4559-8697-6efd5f6866fe)
<br>
<br>
<br>
***2***
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/b169c3e5-83f2-43a8-aaec-a55381a0ebe7)
<br>
<br>
<br>
***3*** You should input empty line after your list
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/5a5d5f04-d066-4233-b580-4b096b6bac62)
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/f53bb128-a81a-45c0-ae64-a429cd63fdec)
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/70dbb94a-2722-4ff3-b70f-ecdd113316bd)
<br>
<br>
<b>In any case you will be able to edit every decision you made<br>
<hr>

![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/2c3f3a14-3465-429a-bac0-475ad1b1c529)
<br>
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/b80db39a-89ba-4d8b-ac47-553062e78445)
<br>
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/5a4c4551-43cb-417f-b3e3-92afacdf0502)
<br>
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/f9e817cd-a595-4643-956b-25b80ac0a09b)
<br>
<br>
<hr>

![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/8d932480-5c04-4773-844d-c780894b7a32)
<br>
![image](https://github.com/M0hamed-Abdelhady/Search-Assistant/assets/112483791/2c1cab45-106f-44cd-a943-160245dc7f44)

## Customization
You can easily customize this utility by modifying the exist_sites list to include additional search sites or by updating the functionality within the Python script.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).


