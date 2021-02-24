# Mission 3: Art Generating Markov Chain 
This project uses a first order Markov Chain to generate a slightly altered version of pixel art. Instead of pixels, a collage like picture made up of dogs is generated -- with each small image of a dog taking the place of a pixel. At the beginning, a first state is randomly selected using a prior probability vector, and each preceeding state is selected based on the probabilities encoded in the transition matrix. 

## Set Up and Running Code. 

1. Go to terminal and clone git repository into a folder on computer  
    ```git clone https://github.com/adrismiller/mission_3.git ```
    
2. Use pip to install necessary requirements for project. 
    ``` pip install requirements.txt```
    
3. Navigate to scripts directory through terminal  
    ``` cd scripts ``` 

4. Run generate.py in command line to randomly generate an image.  
    ```python generate.py``` 
    
5. Run with optional arguments: -i input directory, -od output directory, -o output file, -s sequence length, -d img dimension  
    ```python generate.py -i "input_photos" -od "outputs" -o "my_example_output" -s 400 -d 20```
   
   
   ## Discussion of Project 
   ### Personal Meaning 
   ### Challenges
   ### Creativity 
   ## Sources
   add sources 
