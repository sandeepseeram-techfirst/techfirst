// This is a comment, and is ignored by the compiler

// This helps processing user input
use std::io;

// This is the main function
fn main() {

    // Print text to the console
    println!("Hello, what's your name?");
    let mut name = String::new();

    io::stdin()
        .read_line(&mut name)
        .expect("I'm sorry, but I can't process your name!");

    nice_to_meet_you(name);

}

// Say nice to meet you
fn nice_to_meet_you(username: String) {
    println!("Nice to meet you, {}", username);
}
