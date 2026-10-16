// Processor Housing (Jetson Orin Nano) Parametric CAD Script
module processor_housing() {
    difference() {
        cube([100, 70, 35], center=true);
        translate([0, 0, 5])
            cube([92, 62, 30], center=true);
    }
}
processor_housing();
