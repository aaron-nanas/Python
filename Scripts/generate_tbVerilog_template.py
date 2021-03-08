# To run, go to the directory of the Python file
# Type in the terminal: python <filename>.py
# In this case: python generate_tbVerilog_template.py

template = """//
// <Include module description here>
`timescale 1 ns / 100 ps
`define CLK_PERIOD 10
`include "<filename>.v" // If there are definitions in a separate file, include them here

module NAME_tb( );
    reg INPUT;
    wire OUTPUT;

    NAME UUT( );

// Clock generator with 10 ns period
always #(`CLK_PERIOD/2) CLK = ~CLK;

initial begin

end

endmodule
"""
# The print() adds the trailing newline to make a blank line

if __name__ == "__main__":
    print(template)
