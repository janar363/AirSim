#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "wind_data_processor.h"

namespace py = pybind11;

PYBIND11_MODULE(wind_data_processor, m) {
    py::class_<WindDataProcessor::Position>(m, "Position")
        .def(py::init<>())
        .def_readwrite("x", &WindDataProcessor::Position::x)
        .def_readwrite("y", &WindDataProcessor::Position::y)
        .def_readwrite("z", &WindDataProcessor::Position::z);

    py::class_<WindDataProcessor::WindVal>(m, "WindVal")
        .def(py::init<>())
        .def_readwrite("u", &WindDataProcessor::WindVal::u)
        .def_readwrite("v", &WindDataProcessor::WindVal::v)
        .def_readwrite("w", &WindDataProcessor::WindVal::w);

    py::class_<WindDataProcessor::Array3D>(m, "Array3D")
        .def(py::init<const std::string&, const std::string&, int, int, int, int, int, int>())
        .def("load_data", &WindDataProcessor::Array3D::loadData)
        .def("get_wind_value", &WindDataProcessor::Array3D::getWindValue)
        .def("compute_points_serial_3d_array", &WindDataProcessor::Array3D::computePointsSerial3DArray)
        .def("get_cube_wind_value", &WindDataProcessor::Array3D::getCubeWindValue)
        .def("get_size", &WindDataProcessor::Array3D::getSize)
        .def("print_cube_positions_3d_array_memory_usage", &WindDataProcessor::Array3D::printCubePositions3DArrayMemoryUsage)
        .def("print_memory_usage", &WindDataProcessor::Array3D::printMemoryUsage)
        .def("clear_data", &WindDataProcessor::Array3D::clearData);
}