#General Description of the Project

The project is a web application designed to assist researchers in the initial stages of conducting systematic reviews. Researchers often face the time-consuming and tedious task of screening article titles and abstracts. This app aims to automate part of this process by helping users search through articles based on specific terms and then allowing them to upload the results for further analysis.
Users will upload a text file containing article information (e.g., titles, abstracts, authors) that the app will parse into a structured format with columns for title, authors, year of publication, DOI, etc. The app will integrate with the ChatGPT API to analyze and rate the relevance of each article based on the user’s query. For example, the user may input a description like "I am looking for articles about the correlation between physical activity and academic performance." The app will then scan the uploaded articles and rate their relevancy on a scale from 1 to 10.
Once the articles are rated, the app will provide options to generate graphs (e.g., frequency of relevance ratings), tables, and export the data (e.g., as CSV files). Users can toggle options to select which data to include in their output, allowing for flexible and customizable results.
The app will use Python for the back-end, specifically leveraging libraries like Tkinter for the GUI and the ChatGPT API for processing queries. While the final goal is a web app, initial development may include a command-line interface (CLI) for testing purposes.

#Task Vignettes (User Activity "Flow")
1. Uploading Articles and Parsing Data The researcher begins by using an external tool to search for articles and export the results as a text file. They open the app, click "Upload File," and select the text file containing the article information. Upon uploading, the app parses the file into columns (e.g., title, authors, abstract, year, DOI) and displays this in a table within the app.
Technical details:
- File upload functionality (accept text files).
- Parse the text file into a structured format (CSV or pandas DataFrame).
- Display data in a table format using Tkinter or another GUI framework.

2. Analyzing Articles with ChatGPT The researcher inputs a description of the kind of articles they are looking for (e.g., "Looking for articles discussing the relationship between sleep and cognitive performance"). The app then sends the data to the ChatGPT API to analyze the abstracts for relevance, which results in a rating for each article.
Technical details:
- nAPI integration with ChatGPT.
- Loop through each article, send abstract data to ChatGPT, and receive a relevance score.
- Append the relevance score to a new column in the table.

3. Generating Data Visualizations After the articles have been rated, the researcher clicks on "Generate Graph" and selects the option to create a frequency distribution of relevancy ratings. The app creates a bar graph showing how many articles fall into each relevancy category. The researcher can also generate a table listing all articles with a relevancy score of 10, showing the title, authors, year, and DOI.
Technical details:
- Use Matplotlib or Seaborn to generate graphs.
- Allow the user to filter by relevancy score.
- Provide an option to export tables or graphs to CSV or image format.

4. Downloading the Results The researcher clicks on "Export CSV" to download the filtered list of articles with a relevancy score of 10. They can choose whether to include fields like title, authors, year, and DOI in the CSV.
Technical details:
- Provide an option to download the table data as a CSV file.
- Allow the user to select which fields to include in the export.

#Technical "Flow"
1. File upload and parsing: Users upload a text file containing information about the articles. The text is read and parased into a pandas DataFrame, with columns for each field (title, authors, abstract, year, DOI). This will incolve some text parsing logic to identify each filed and correctly split the dat into rows and columns.
2. ChatGPT API integration: The app will use OpenAI API to send abstracts, titles and the user's query. ChatGPT will return a relevance score for each article, which will be integrated to the DataFrame.
3. Data visualization: Once relevance scores are generated, the app will provide options to generate different visualizations using Matplotlib (or other suggested alternatives). This could include bar graphs for relevance scores, tables of top-rated relevance articles, etc)
4. User interface (GUI): Tkinter will be used to create a simple GUI for file upload, query input, and data visualization. The app will contain buttons to upload file, input the query, options that users can toggle to generate tables or graphs.
5. Data export: The final processed data with the relevance scores can be exported as a csv file. Users will have the option to select specific columns for export as ell.

#Technical Blocks:
- File upload & parsing: Text file --> pandas DataFrame
- ChatGPT API: Abstracts and user query --> Relevance scores.
- Visualization: DataFrame --> Graphs & tables
- Export: DataFrame --> csv file output
