```openscad
// Micro Camera Mount Parametric CAD Script (OpenSCAD representation for STL compilation)
module camera_mount() {
    difference() {
        cube([20, 20, 10], center=true);
        cylinder(h=12, r=8, center=true);
    }
}
camera_mount();