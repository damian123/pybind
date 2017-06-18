#include <pybind11/pybind11.h>

namespace py = pybind11;

double add(double i, double j) {
	return i + j;
}

PYBIND11_MODULE(example, m) {
	m.doc() = "pybind11 example plugin"; // optional module docstring

	m.def("add", &add, "A function which adds two numbers");
}