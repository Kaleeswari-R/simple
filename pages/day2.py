import streamlit as st

st.title("2nd day")

# Dropdown for selecting topics
selected_option = st.selectbox("Select Topic", ["Control Statements", "Patterns", "Mathematical Calculations"])

# Function to show control statements example
def show_control_statements():
    st.header("Control Statements Example")
    st.code("""
    public class ControlStatementsExample {
        public static void main(String[] args) {
            int number = 10;
            if (number > 0) {
                System.out.println("The number is positive.");
            } else {
                System.out.println("The number is non-positive.");
            }
        }
    }
    """)

# Function to show patterns example
def show_patterns():
    st.header("Patterns Example")
    st.code("""
    public class PatternsExample {
        public static void main(String[] args) {
            for (int i = 1; i <= 5; i++) {
                for (int j = 1; j <= i; j++) {
                    System.out.print("* ");
                }
                System.out.println();
            }
        }
    }
    """)

# Function to show mathematical calculations example
def show_mathematical_calculations():
    st.header("Mathematical Calculations Example")
    st.code("""
    public class MathCalculationsExample {
        public static void main(String[] args) {
            int a = 10;
            int b = 5;
            int sum = a + b;
            int product = a * b;
            System.out.println("Sum: " + sum);
            System.out.println("Product: " + product);
        }
    }
    """)

# Main function to display content based on the selected option
def main():
    if selected_option == "Control Statements":
        show_control_statements()
    elif selected_option == "Patterns":
        show_patterns()
    elif selected_option == "Mathematical Calculations":
        show_mathematical_calculations()

if __name__ == "__main__":
    main()
