# researchdoor

## Project requirements

Aplikacja Django dla grup badawczych / instytutów naukowych [3 osoby].
Serwis ma umożliwiać tworzenie stron www dla grup naukowych (patrz np. http://gmum.net),
gdzie podstawową funkcjonalnością jest:

1. tworzenie newsów
2. uzupełnianie listy seminariów
3. dodawanie statycznych stron z tekstem
4. strony pracownicze [edytowalne również przez samych pracowników], czyli profile gdzie umieszczają swoje dane osobowe;
konferencje w których uczestniczyli; publikacje które napisali - istotnym modułem będzie by publikacje były
automatycznie synchronizowane ze scholar.google.com, dblp, ew. innymi bazami podobnie jak to się dzieje na takich serwisach
jak researchgate.com - czyli pobierana jest informacja o napisaniu pracy przez osobę o danym imieniu i nazwisku i użytkownik
ma w swoim profilu “sugestię” że to jego/jej praca - może zaakceptować lub odrzucić.
graficzne prezentowanie dostępności członków zakładu (patrz zakładka kontakt gmum.net)


## Deployment

* create a fork of the main repo and check it out
* set upstream
    
    ```sh
    git remote add upstream git@github.com:DoWithoutGirls/researchdoor.git
    ```
    
* when working on a new feature create a new local branch

    ```sh
    git checkout develop
    
    git checkout -b RD-1-example-task
    
    git push -u origin RD-1-example-task
    ```
* keep your brach up-to-date with develop branch
* when finishing your task create a pull request
    
