# ICAV
Solution to the technical assessment for ICAV interview process.

Two endpoints created for our flask application which reads the data from a csv file.
First endpoint takes an input in the URL endpoint for number of rows to be read from the file.
Second enpoint takes a string input in the URL endpoint for filtering the entered data in the books record and returning filtered books.

Endpoint URL examples:
1. 127.0.0.1/5000/4 (If 4 rows are required to be read)
2. 127.0.0.1/5000/filter/1992 (If all the books from 1992 pubyear are required to be filtered)
