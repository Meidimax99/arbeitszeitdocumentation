# This is the control flow how it should be, not how it is at the moment

# Modules 

## Main Module

* Process Command line arguments
* Determine Days that are elegible for work (No Holiday, No Sunday, ideally also no Saturday)
* Iterate through the rows and fill in time to work
  * Would be best to not even iterate through the rows, but to just add the days to a list
* Use a normal distribution to have some variance in the time worked daily
* Verify that enough hours a locked in after filling forms, if not, just retry with different random seed

## Interface for the form
* Specific interface for the specific form
* should abstract from the access to the specific rows and ids of the form
* should abstract from different documents and different rows, should just enable to add another entry
    * if the document is full nothing should be done externally to create another document
