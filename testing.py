import unittest
from operations import *

# transpose(matrix) row(matrix,row_number col(matrix,col_number)
# identity(n) m_multiply(a, b) m_power(matrix, n)
# swap(matrix, row_1, row_2) add_multiple(matrix, row_1, factor, row_2)
# multiply_const(matrix, row_1, factor)
# ref(matrix) rref(matrix) det(matrix) inverse(matrix)
class TestOperations(unittest.TestCase):
    invertible_square_matrix_a=[[1,3,5],[7,11,13],[17,19,23]]
    invertible_square_matrix_b=[[1,-3,5],[2,-1,8],[4,2,9]]
    singular_square_matrix_c=[[1,2,3],[4,5,6],[7,8,9]]
    symmetric_matrix_d=[[1,2,3],[2,0,5],[3,5,-4]]
    a=[[1,2,3],[4,5,6]]
    b=[[5,6],[7,8]]
    # big_matrix_10_10_e=[
    #     [1,2,3,4,5,6,7,8,9],
    #     [-2,-3,-4,-5,-6,-7,-8,-9,-1],
    #     [],
    #     [],
    #     [],
    #     [],
    #     [],
    #     [],
    #     [],
    #     []
    # ]
    rectangular_matrix_4_3_f=[[-8,-6,5],[2,3,6],[-10,8,4],[8,4,-5]]
    rectangular_matrix_3_4_g=[[1,6,4],[6,-2,-8],[-7,3,-1],[-8,-7,9]]
    #orthagonal_matrix_g=


    def setUp(self):
        pass

    def test_transpose(self):
        self.assertEqual(transpose(TestOperations.invertible_square_matrix_a),[[1,7,17],[3,11,19],[5,13,23]])
        self.assertEqual(transpose(TestOperations.symmetric_matrix_d),TestOperations.symmetric_matrix_d)

    def test_m_multiply(self):
        self.assertEqual(m_multiply(
            TestOperations.invertible_square_matrix_a, TestOperations.invertible_square_matrix_b),
            [[27,4,74],[81,-6,240],[147,-24,444]])
        self.assertEqual(m_multiply(
            TestOperations.invertible_square_matrix_a, TestOperations.rectangular_matrix_4_3_f
            ), False)
        self.assertEqual(m_multiply(
            TestOperations.rectangular_matrix_4_3_f, TestOperations.invertible_square_matrix_a
            ),[[35,5,-3],[125,153,187],[114,134,146],[-49,-27,-23]])

if __name__ == '__main__':
    unittest.main()