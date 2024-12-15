# shell script grep and sed commands

host .devcontainer for practice/executing shell script

## sed

1. replace string in .txt

    ```shell
    sed s'/Rama/Hari/' text.txt   #replace string and display output in terminal (it will not override values in file)
    sed -i s'/Rama/Hari/' text.txt #s:string, -i will override string in .txt file
    ```

2. delete line in .txt

    ```shell
    sed -i '/this line is will get deleted using sed/d' text.txt
    ```  

3. insert and append before or after the text

    ```shell
    sed '/Rama/i Hari' text.txt  #i: insert (insert before string)
    sed '/Rama/a Hari' text.txt  #a: append (append after string
    ```

4. display specific line from file

    ```shell
    sed -n '/Rama/p' text.txt   #p:print the line where Rama is mentioned
    ```

5. display line number of word (n for number, e for expression)

    ```shell
    sed -n -e '/word/=' filename
    ```

6. display line number along with word (n for number, e for expression)

    ```shell
    sed -n -e '/word/=' -e /'word/p' filename
    ```

7. replace words, only from 1st to 5th lines (g for global)   #to override values in file use (-i after sed)

    ```bash
    sed '1,5 s/word/replace-word/g' filename
    ```

8. search word from file (-i used for ignore-case sensitive, n=line number)

    ```shell
    ## syntax
    grep -in term /path/to/file
    grep -rin term /path/to/folder

    #example
    grep -in "search-word" filename.txt filename2.txt
    ```

9. search filename using grep

    ```shell
    ls | grep -in "filename" or ls | grep -in ".txt"
    ```

10. Search word Recursively (used for dir and subdir) in Directories:
r=recursive , i=ignore, n=line number

    ```shell
    grep -rin "search-word" /directory-name
    ```

11. search for file names recursively in the current directory and its subdirectories using find

    ```bash
    find . -type f | grep ".sh"
    ```

12. count the number of times word used in file (c used of count)

    ```bash
    grep -ic rama text.txt condition.sh
    ```
