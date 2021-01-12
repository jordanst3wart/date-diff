# date-diff

### To Run

To run the CLI try (requires docker):
```shell
chmod +x run.sh
./run.sh docker_build_cli
./run.sh cli -s 1983-06-02 -e 1983-06-22
# Day difference: 19
```

If you have python installed you can try
```shell
chmod +x date-diff
./date-diff -s 1983-06-02 -e 1983-06-22
# Day difference: 19
```

### Assumptions
- assume return a negative date difference is fine
- assume same date has 0 difference, not just adjacent days. 
- throw an error if the start date is before 1901, or after 2999
- throw an error if invalid date  
- assuming Gegorian calendar

### Program design:
cli interface -> date model -> leap year functions

Break leap year into separate concern, following Single responsibility.


### Rationale for Python:
- good cli library
- good with dealing with data
- fast development
- less code


### Requirements
- provide examples of how to use CLI
- accept input from the cli
- cannot use native date or calendar classes
- cater for all valid dates between 1901-01-01 and 2999-12-31
- can i use cli helper tools?

### Things to consider: Leap years
- 4 year leap year rule
- 100 year leap year rule
- 400 year leap year rule
ie. 2000 was a leap year, due to it was part of the 400 year rule
whereas 1900 was not
  