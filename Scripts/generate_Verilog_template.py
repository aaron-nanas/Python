# To run, go to the directory of the Python file
# Type in the terminal: python <filename>.py
# In this case: python generate_Verilog_template.py

skeleton = """//

// <Include module description here>

`timescale 1 ns / 100 ps
`define
`include "<filename>.v" // If there are definitions in a separate file, include them here

module NAME( );
    // Module declarations
    parameter PARAM_NAME = 0;

    input CLK;                          
    input RESET;

    output OUT;

    initial begin
        output = input;
    end

// Comment for next block

    always @(*) begin
        output <= input;
    end

endmodule
"""
# The print() adds the trailing newline to make a blank line

if __name__ == "__main__":
    print(skeleton)
