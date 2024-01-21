import streamlit as st

st.title("1st day")
selected_option = st.selectbox("Select Topic", ["Introduction", "Data Types", "Variables & Constants"])

def show_introduction():
    st.header("Introduction")
    st.write("""
     Introduction to Java:
            Java is a high-level, versatile, and object-oriented programming language developed by Sun Microsystems (now owned by Oracle). It was designed with the primary goal of being platform-independent, allowing developers to write code once and run it on any device that supports Java. This feature is achieved through the use of the Java Virtual Machine (JVM), which interprets and executes Java bytecode.
    """)

def show_datatypes():
    st.header("Data Types")
    st.write("""
    public class SimpleExample {

    public static void main(String[] args) {
        int age = 25;
        double height = 5.8;
        char gender = 'M';
        boolean isStudent = true;
        String name = "John";
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Gender: " + gender);
        System.out.println("Is Student: " + isStudent);
    }
}

    """)

def show_variables_and_constants():
    st.header("Variables & Constants")
    st.code("""public class BasicExample {
    public static final String GREETING = "Hello, ";
    public static void main(String[] args) {
        String name = "World";
        String message = GREETING + name;
        System.out.println(message);
        name = "Java";
        System.out.println(GREETING + name);
    }
}
""")

def main():
    if selected_option == "Introduction":
        show_introduction()
    elif selected_option == "Data Types":
        show_datatypes()
    elif selected_option == "Variables & Constants":
        show_variables_and_constants()

if __name__ == "__main__":
    main()
