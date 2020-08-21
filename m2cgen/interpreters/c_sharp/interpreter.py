import os

from m2cgen import ast
from m2cgen.interpreters import mixins
from m2cgen.interpreters import utils
from m2cgen.interpreters.interpreter import ImperativeToCodeInterpreter
from m2cgen.interpreters.c_sharp.code_generator import CSharpCodeGenerator


class CSharpInterpreter(ImperativeToCodeInterpreter,
                        mixins.LinearAlgebraMixin,
                        mixins.SubroutinesMixin):

    supported_bin_vector_ops = {
        ast.BinNumOpType.ADD: "AddVectors",
    }

    supported_bin_vector_num_ops = {
        ast.BinNumOpType.MUL: "MulVectorNumber",
    }

    abs_function_name = "Abs"
    exponent_function_name = "Exp"
    logarithm_function_name = "Log"
    log1p_function_name = "Log1p"
    power_function_name = "Pow"
    sqrt_function_name = "Sqrt"
    tanh_function_name = "Tanh"
    set_contains_function_name = "Contains"

    with_log1p_expr = False

    def __init__(self, namespace="ML", class_name="Model", indent=4,
                 function_name="Score", *args, **kwargs):
        self.namespace = namespace
        self.class_name = class_name
        self.indent = indent
        self.function_name = function_name

        super().__init__(cg, *args, **kwargs)

    def interpret(self, expr):
        top_cg = self.create_code_generator()


        method_name = self.function_name
        args = [(True, self._feature_array_name)]

        with top_cg.namespace_definition(self.namespace):
            with top_cg.class_definition(self.class_name):
                
                self.enqueue_subroutine(self.function_name, expr)
                self.process_subroutine_queue(top_cg)
                
                if self.with_linear_algebra:
                    filename = os.path.join(
                        os.path.dirname(__file__), "linear_algebra.cs")
                    top_cg.add_code_lines(utils.get_file_content(filename))

                if self.with_log1p_expr:
                    filename = os.path.join(
                        os.path.dirname(__file__), "log1p.cs")
                    top_cg.add_code_lines(utils.get_file_content(filename))

                for _, item_set in self.static_declarations:
                    top_cg.add_code_line(item_set)

        top_cg.add_dependency("System.Collections.Generic")
        if self.with_math_module:
            top_cg.add_dependency("System.Math")

        return top_cg.finalize_and_get_generated_code()

    # def interpret_contains_int_expr(self, expr, **kwargs):
    #     pass

    def interpret_log1p_expr(self, expr, **kwargs):
        self.with_log1p_expr = True
        return super().interpret_log1p_expr(expr, **kwargs)

    
    def create_code_generator(self):
        return CSharpCodeGenerator(self.indent)
