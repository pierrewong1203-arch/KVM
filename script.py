#Line 12 (Name), 15(RAM), 16(RAM), 17(RAM), 20(CPU), 24(CPU), 25(CPU), 26(CPU), 29(BIOS), 30(BIOS), 32(BIOS mode), 57(Disk Size), 69(ISO Path)

vm_domain_type = r"kvm" #Hardware Boost is "kvm", full emu (extremely slow) is "qemu", Xen back is "xen", linux container is "lxc", Parallels back is "parallels", FreeBSD bhyve back is "bhyve", OpenVZ container is "vz".

# KVM and QEMU both rely on the QEMU emulator binary (e.g. /usr/libexec/qemu-kvm on RHEL).
# If left empty, libvirt will attempt to resolve the default binary path automatically.
if vm_domain_type in [r"kvm", r"qemu"]:
    vm_emu = r"/usr/libexec/qemu-kvm"
else:
    vm_emu = r""

vm_name = "Test VM".replace(" ", "_")
vm_uuid = r"" # Leave empty so KVM/libvirt auto-generates a UUID

vm_ram_unit = r"GiB" #KB is "KiB", MB is "MiB", GiB is "GiB", TiB is "TiB", K is "K", M is "M", G is "G", T is "T".
vm_memory_amount = r"4"
vm_current_memory_amount = r"4"

vm_cpu_placement = r"static" #Fixed is "static", can add/remove when running is "auto".
vm_vcpu_amount = r"4" #Must Equal To socket*cores*threads.

vm_cpu_mode = r"host-passthrough" #Pass-though host cpu is "host-passthrough", choose most same as host is "host-model", custom is "custom".
vm_cpu_check = r"none" #Check mode is "none", partial is "partial", full is "full".
vm_cpu_socket = r"1"
vm_cpu_cores = r"2"
vm_cpu_threads = r"2"

vm_firmware = r"efi" #UEFI is "efi", BIOS is "bios".
vm_arch = r"x86_64" #64bit is "x86_64", 32bit is "i686", arm64 is "aarch64", arm32 is "armv7l", PowerPC x32 is "ppc", PowerPC Big End is "ppc64", PowerPC Small End is "ppc64le", IBM Big x31 is "s390", IBM Big x64 is "s390x", MIPS is "mips", Sparc is "sparc".
vm_machine = r"q35" #Modern PCIe is "q35", Legacy i440fx is "pc", Arm is "virt", Lite VM is "microvm".
vm_virt_type = r"hvm" #Kvm full virt. is "hvm", Xen half virt. is "xenpv", Xen full virt. is "xenfv".
if vm_firmware == r"efi":
    vm_secure = r"no" #Enable or Disable Secure Boot, "yes" or "no".

#vm_boot_device = r"hd" #Harddisk is "hd", CD/DVD is "cdrom", PXE is "network", floppydisk is "fd".

vm_features_acpi = True #Enable ACPI, True or False.
vm_features_apic = True #Enable APIC, True or False.
vm_vmport = "off" #VMware Port emu, "on" or "off".

vm_clock_offset = r"localtime" #UTC time is "utc", local time is "localtime", special timezone is "timezone", variable is "variable".
if vm_clock_offset == r"timezone":
    vm_timezone_name = r"Asia/Shanghai" #Timezone string format, e.g., "America/New_York", "Asia/Shanghai".
vm_timer_rtc = r"catchup" #RTC tick policy is "catchup", delay is "delay", merge is "merge", discard is "discard".
vm_timer_pit = r"delay" #PIT tick policy is "catchup", delay is "delay", merge is "merge", discard is "discard".
vm_timer_hpet = r"no" #HPET present, "yes" or "no".

vm_disk_type = r"file" #File image is "file", block device is "block", network storage is "network", libvirt volume is "volume", directory is "dir", virtual FAT is "vvfat".
vm_disk_device = r"disk" #Disk is "disk", CD/DVD is "cdrom", floppy is "floppy", LUN is "lun".
vm_disk_driver_name = r"qemu" #Driver name is "qemu".
vm_disk_driver_type = r"qcow2" #QEMU copy-on-write is "qcow2", raw format is "raw", VMware is "vmdk", VirtualBox is "vdi", Hyper-V is "vhd", QEMU enhanced is "qed", old QEMU is "qcow".
vm_disk_driver_cache = r"none" #No cache is "none", direct sync is "directsync", write through is "writethrough", write back is "writeback", unsafe is "unsafe".
vm_disk_driver_io = r"native" #Linux native AIO is "native", thread pool is "threads", Linux io_uring is "io_uring".

# Dynamically set disk image path based on vm_name, decoupled from memory size
vm_disk_source_file = rf"/var/lib/libvirt/images/pool/{vm_name}.qcow2" #Disk image absolute path string based on vm_name.
vm_disk_size = r"64G" # Independent hard disk storage size configuration, separated from RAM allocation.

vm_disk_target_dev = r"sda" #Virtio bus is vd[a-z], SATA/SCSI is sd[a-z], IDE is hd[a-z], Xen is xvd[a-z].
vm_disk_target_bus = r"sata" #Virtio is "virtio", SCSI is "scsi", SATA is "sata", IDE is "ide", USB is "usb", Xen is "xen".
vm_disk_logical_block_size = r"512" #Logical block size: "512" or "4096".
vm_disk_physical_block_size = r"512" #Physical block size: "512" or "4096".
vm_disk_boot_order = r"1" #Boot order positive integer.

vm_cdrom_type = r"file" #File image is "file".
vm_cdrom_device = r"cdrom" #CD/DVD device is "cdrom".
vm_cdrom_driver_name = r"qemu" #Driver name is "qemu".
vm_cdrom_driver_type = r"raw" #Raw format is "raw".
vm_cdrom_source_file = r"/var/lib/libvirt/images/en_windows_10_enterprise_ltsc_2019_x64_dvd_5795bb03.iso" #ISO file absolute path string.
vm_cdrom_target_dev = r"sdb" #Target device is sda.
vm_cdrom_target_bus = r"sata" #Target bus is "sata", "ide", or "scsi".
vm_cdrom_boot_order = r"2" #Boot order positive integer.

vm_net_type = r"network" #Libvirt virtual network is "network", bridge is "bridge", MacVTap direct is "direct", user mode is "user", PCI hostdev is "hostdev", multicast is "mcast", TCP server is "server", TCP client is "client".
vm_net_source = r"default" #Libvirt network name string.
vm_net_model = r"e1000" #Virtio is "virtio", Intel Gigabit is "e1000" or "e1000e", Realtek is "rtl8139", NE2000 is "ne2k_pci", AMD PCnet is "pcnet", VMware vmxnet3 is "vmxnet3".

vm_graphics_type = r"vnc" #VNC protocol is "vnc", SPICE is "spice", SDL local window is "sdl", headless EGL is "egl-headless", local desktop is "desktop", RDP export is "rdpexport".
vm_graphics_port = r"-1" #Auto assign is "-1", manual port is 5900-5999.
vm_graphics_autoport = r"yes" #Auto port is "yes" or "no".
vm_graphics_listen = r"127.0.0.1" #Listen IP address string.
vm_graphics_listen_type = r"address" #Address is "address", network is "network", Unix socket is "socket".

vm_video_model = r"vga" #SPICE recommended is "qxl", generic VGA is "vga", paravirtualized GPU is "virtio", Cirrus is "cirrus", GPU passthrough is "gpu", none is "none".
vm_video_vram = r"65536" #VRAM size in KB positive integer.
vm_video_heads = r"1" #Display heads positive integer.

vm_input_tablet_bus = r"usb" #Tablet bus is "usb", "ps2", "virtio", or "xen".
vm_input_mouse_bus = r"ps2" #Mouse bus is "ps2", "usb", "virtio", or "xen".

vm_controller_usb_model = r"qemu-xhci" #USB 3.0 is "qemu-xhci", USB 2.0 is "ich9-ehci1", USB 1.1 is "ich9-uhci1".
vm_controller_scsi_model = r"virtio-scsi" #Paravirtualized SCSI is "virtio-scsi", LSI Logic is "lsilogic".

vm_serial_type = r"pty" #Pseudo terminal is "pty", file is "file", TCP is "tcp", Unix socket is "unix", null is "null", stdio is "stdio", virtual console is "vc", physical device is "dev", pipe is "pipe".
vm_serial_port = r"0" #Serial port number non-negative integer.

vm_console_type = r"pty" #Pseudo terminal is "pty".
vm_console_target_type = r"serial" #Serial console is "serial", paravirtualized console is "virtio", guestfwd is "guestfwd", Xen console is "xen".
vm_console_target_port = r"0" #Console port number non-negative integer.

vm_memballoon_model = r"virtio" #Paravirtualized balloon driver is "virtio", disabled is "none".

vm_on_poweroff = r"destroy" #Poweroff action is "destroy", restart is "restart", preserve is "preserve", rename-restart is "rename-restart".
vm_on_reboot = r"restart" #Reboot action is "destroy", restart is "restart", preserve is "preserve", rename-restart is "rename-restart".
vm_on_crash = r"destroy" #Crash action is "destroy", restart is "restart", preserve is "preserve", coredump-destroy is "coredump-destroy", coredump-restart is "coredump-restart".


# --- Detailed Part-by-Part Verification with Cross-Dependency Checks ---

validation_errors = []

# 1. Verify Domain Type & Virt Type Linkage
valid_domain_types = ["kvm", "qemu", "xen", "lxc", "parallels", "bhyve", "vz"]
if vm_domain_type not in valid_domain_types:
    validation_errors.append(f"[Domain Section] Invalid domain type: '{vm_domain_type}'. Expected one of {valid_domain_types}.")

valid_virt_types = ["hvm", "xenpv", "xenfv"]
if vm_virt_type not in valid_virt_types:
    validation_errors.append(f"[OS Section] Invalid virtualization type: '{vm_virt_type}'. Expected one of {valid_virt_types}.")

if vm_domain_type in ["kvm", "qemu"] and vm_virt_type in ["xenpv", "xenfv"]:
    validation_errors.append(f"[OS/Domain Linkage Error] Domain type '{vm_domain_type}' cannot be paired with virtualization type '{vm_virt_type}' (Xen types require domain type 'xen').")
elif vm_domain_type == "xen" and vm_virt_type == "hvm":
    validation_errors.append(f"[OS/Domain Linkage Error] Domain type 'xen' with virt type 'hvm' is invalid; use 'xenfv' instead.")

# 2. Verify VM Name & UUID
if not vm_name or any(c in vm_name for c in " "):
    validation_errors.append(f"[Identity Section] Invalid VM name '{vm_name}': cannot be empty or contain spaces.")

# 3. Verify Memory Settings
valid_ram_units = ["KiB", "MiB", "GiB", "TiB", "K", "M", "G", "T"]
if vm_ram_unit not in valid_ram_units:
    validation_errors.append(f"[Memory Section] Invalid memory unit '{vm_ram_unit}'. Expected one of {valid_ram_units}.")
try:
    if int(vm_memory_amount) <= 0 or int(vm_current_memory_amount) <= 0:
        raise ValueError()
except ValueError:
    validation_errors.append("[Memory Section] Memory amounts must be positive integers.")

# 4. Verify CPU Topology & VCPUs
try:
    calc_vcpu = int(vm_cpu_socket) * int(vm_cpu_cores) * int(vm_cpu_threads)
    if calc_vcpu != int(vm_vcpu_amount):
        validation_errors.append(f"[CPU Section] Topology mismatch: sockets({vm_cpu_socket}) * cores({vm_cpu_cores}) * threads({vm_cpu_threads}) = {calc_vcpu}, which does not equal vcpu total ({vm_vcpu_amount}).")
except ValueError:
    validation_errors.append("[CPU Section] CPU count and topology parameters must be valid integers.")

# 5. Verify OS, Firmware, Arch, and Machine Linkage
valid_firmwares = ["efi", "bios"]
if vm_firmware not in valid_firmwares:
    validation_errors.append(f"[OS Section] Invalid firmware '{vm_firmware}'. Expected 'efi' or 'bios'.")
if vm_firmware == "efi" and ('vm_secure' not in globals() and 'vm_secure' not in locals()):
    validation_errors.append("[OS Section] EFI firmware is enabled, but 'vm_secure' variable for Secure Boot is missing.")

if vm_arch == "x86_64" and vm_machine == "virt":
    validation_errors.append("[OS Section] Architecture and Machine Mismatch: 'x86_64' cannot use machine type 'virt' (which is strictly for ARM architecture).")
elif vm_arch in ["aarch64", "armv7l"] and vm_machine in ["q35", "pc"]:
    validation_errors.append(f"[OS Section] Architecture and Machine Mismatch: ARM architecture ('{vm_arch}') cannot use x86 machine type '{vm_machine}'.")

# 6. Verify Clock & Timezone Conditional Settings
valid_clocks = ["utc", "localtime", "timezone", "variable"]
if vm_clock_offset not in valid_clocks:
    validation_errors.append(f"[Clock Section] Invalid clock offset '{vm_clock_offset}'. Expected one of {valid_clocks}.")
if vm_clock_offset == "timezone":
    if 'vm_timezone_name' not in globals() and 'vm_timezone_name' not in locals():
        validation_errors.append("[Clock Section] Clock offset is set to 'timezone', but the required 'vm_timezone_name' variable is missing (e.g., format like 'Asia/Shanghai').")

# 7. Verify Disk Storage Configuration & Dev-Bus Linkage (Hard Disk)
valid_disk_caches = ["none", "directsync", "writethrough", "writeback", "unsafe"]
if vm_disk_driver_cache not in valid_disk_caches:
    validation_errors.append(f"[Disk Section] Invalid cache mode '{vm_disk_driver_cache}'. Expected one of {valid_disk_caches}.")

if vm_disk_target_bus == "virtio" and not vm_disk_target_dev.startswith("vd"):
    validation_errors.append(f"[Disk Section] Dev/Bus Linkage Error (Disk): Bus 'virtio' requires target device prefix 'vd' (e.g., 'vda'), but got '{vm_disk_target_dev}'.")
elif vm_disk_target_bus in ["sata", "scsi"] and not vm_disk_target_dev.startswith("sd"):
    validation_errors.append(f"[Disk Section] Dev/Bus Linkage Error (Disk): Bus '{vm_disk_target_bus}' requires target device prefix 'sd' (e.g., 'sda'), but got '{vm_disk_target_dev}'.")
elif vm_disk_target_bus == "ide" and not vm_disk_target_dev.startswith("hd"):
    validation_errors.append(f"[Disk Section] Dev/Bus Linkage Error (Disk): Bus 'ide' requires target device prefix 'hd' (e.g., 'hda'), but got '{vm_disk_target_dev}'.")

# 8. Verify CD-ROM Configuration & Dev-Bus Linkage
if vm_cdrom_target_bus == "virtio" and not vm_cdrom_target_dev.startswith("vd"):
    validation_errors.append(f"[CD-ROM Section] Dev/Bus Linkage Error (CD-ROM): Bus 'virtio' requires target device prefix 'vd' (e.g., 'vda'), but got '{vm_cdrom_target_dev}'.")
elif vm_cdrom_target_bus in ["sata", "scsi"] and not vm_cdrom_target_dev.startswith("sd"):
    validation_errors.append(f"[CD-ROM Section] Dev/Bus Linkage Error (CD-ROM): Bus '{vm_cdrom_target_bus}' requires target device prefix 'sd' (e.g., 'sda'), but got '{vm_cdrom_target_dev}'.")
elif vm_cdrom_target_bus == "ide" and not vm_cdrom_target_dev.startswith("hd"):
    validation_errors.append(f"[CD-ROM Section] Dev/Bus Linkage Error (CD-ROM): Bus 'ide' requires target device prefix 'hd' (e.g., 'hda'), but got '{vm_cdrom_target_dev}'.")

# Output detailed validation results
if validation_errors:
    print("[-] Configuration Verification Failed with Detailed Errors:")
    for err in validation_errors:
        print(f"    {err}")
    print("\nPlease correct the corresponding variables above before generating the XML text.")
else:
    print("[+] All configuration parts verified successfully with no errors!\n")


# --- Disk Generation Command Part ---

disk_gen_command = f"qemu-img create -f {vm_disk_driver_type} {vm_disk_source_file} {vm_disk_size}"
print(f"[i] Recommended disk generation command for your VM:")
print(f"    {disk_gen_command}\n")


# --- XML Generator Part ---

xml_parts = []

# Domain Root and Identity
domain_attrs = f"type='{vm_domain_type}'"
xml_parts.append(f"<domain {domain_attrs}>")
xml_parts.append(f"  <name>{vm_name}</name>")
if vm_uuid:
    xml_parts.append(f"  <uuid>{vm_uuid}</uuid>")

# Memory Section
xml_parts.append(f"  <memory unit='{vm_ram_unit}'>{vm_memory_amount}</memory>")
xml_parts.append(f"  <currentMemory unit='{vm_ram_unit}'>{vm_current_memory_amount}</currentMemory>")

# CPU Section
xml_parts.append(f"  <vcpu placement='{vm_cpu_placement}'>{vm_vcpu_amount}</vcpu>")
xml_parts.append(f"  <cpu mode='{vm_cpu_mode}' check='{vm_cpu_check}'>")
xml_parts.append(f"    <topology sockets='{vm_cpu_socket}' cores='{vm_cpu_cores}' threads='{vm_cpu_threads}'/>")
xml_parts.append(f"  </cpu>")

# OS / Firmware Section
os_line = f"  <os firmware='{vm_firmware}'>"
xml_parts.append(os_line)
xml_parts.append(f"    <type arch='{vm_arch}' machine='{vm_machine}'>{vm_virt_type}</type>")
if vm_firmware == r"efi":
    xml_parts.append(f"    <loader secure='{vm_secure}'/>")
#xml_parts.append(f"    <boot dev='{vm_boot_device}'/>")
xml_parts.append(f"  </os>")

# Features Section
xml_parts.append(f"  <features>")
if vm_features_acpi:
    xml_parts.append(f"    <acpi/>")
if vm_features_apic:
    xml_parts.append(f"    <apic/>")
xml_parts.append(f"    <vmport state='{vm_vmport}'/>")
xml_parts.append(f"  </features>")

# Clock Section with Conditional Timezone support
if vm_clock_offset == r"timezone" and 'vm_timezone_name' in locals():
    xml_parts.append(f"  <clock offset='{vm_clock_offset}' timezone='{vm_timezone_name}'>")
else:
    xml_parts.append(f"  <clock offset='{vm_clock_offset}'>")
xml_parts.append(f"    <timer name='rtc' tickpolicy='{vm_timer_rtc}'/>")
xml_parts.append(f"    <timer name='pit' tickpolicy='{vm_timer_pit}'/>")
xml_parts.append(f"    <timer name='hpet' present='{vm_timer_hpet}'/>")
xml_parts.append(f"  </clock>")

# Devices Section
xml_parts.append(f"  <devices>")

# Conditional Emulator Path
if vm_emu:
    xml_parts.append(f"    <emulator>{vm_emu}</emulator>")

# Disk (Using vm_name dynamically for source file path and conditional blockio inclusion for virtio/scsi buses)
xml_parts.append(f"    <disk type='{vm_disk_type}' device='{vm_disk_device}'>")
xml_parts.append(f"      <driver name='{vm_disk_driver_name}' type='{vm_disk_driver_type}' cache='{vm_disk_driver_cache}' io='{vm_disk_driver_io}'/>")
xml_parts.append(f"      <source file='{vm_disk_source_file}'/>")
xml_parts.append(f"      <target dev='{vm_disk_target_dev}' bus='{vm_disk_target_bus}'/>")
if vm_disk_target_bus in ["virtio", "scsi"]:
    xml_parts.append(f"      <blockio logical_block_size='{vm_disk_logical_block_size}' physical_block_size='{vm_disk_physical_block_size}'/>")
xml_parts.append(f"      <boot order='{vm_disk_boot_order}'/>")
xml_parts.append(f"    </disk>")

# CDROM
xml_parts.append(f"    <disk type='{vm_cdrom_type}' device='{vm_cdrom_device}'>")
xml_parts.append(f"      <driver name='{vm_cdrom_driver_name}' type='{vm_cdrom_driver_type}'/>")
xml_parts.append(f"      <source file='{vm_cdrom_source_file}'/>")
xml_parts.append(f"      <target dev='{vm_cdrom_target_dev}' bus='{vm_cdrom_target_bus}'/>")
xml_parts.append(f"      <readonly/>")
xml_parts.append(f"      <boot order='{vm_cdrom_boot_order}'/>")
xml_parts.append(f"    </disk>")

# Network
xml_parts.append(f"    <interface type='{vm_net_type}'>")
xml_parts.append(f"      <source network='{vm_net_source}'/>")
xml_parts.append(f"      <model type='{vm_net_model}'/>")
xml_parts.append(f"    </interface>")

# Graphics
xml_parts.append(f"    <graphics type='{vm_graphics_type}' port='{vm_graphics_port}' autoport='{vm_graphics_autoport}' listen='{vm_graphics_listen}'>")
xml_parts.append(f"      <listen type='{vm_graphics_listen_type}' address='{vm_graphics_listen}'/>")
xml_parts.append(f"    </graphics>")

# Video
xml_parts.append(f"    <video>")
xml_parts.append(f"      <model type='{vm_video_model}' vram='{vm_video_vram}' heads='{vm_video_heads}'/>")
xml_parts.append(f"    </video>")

# Input
xml_parts.append(f"    <input type='tablet' bus='{vm_input_tablet_bus}'/>")
xml_parts.append(f"    <input type='mouse' bus='{vm_input_mouse_bus}'/>")

# Controllers
xml_parts.append(f"    <controller type='usb' index='0' model='{vm_controller_usb_model}'/>")
xml_parts.append(f"    <controller type='scsi' index='0' model='{vm_controller_scsi_model}'/>")

# Serial & Console
xml_parts.append(f"    <serial type='{vm_serial_type}'>")
xml_parts.append(f"      <target port='{vm_serial_port}'/>")
xml_parts.append(f"    </serial>")
xml_parts.append(f"    <console type='{vm_console_type}'>")
xml_parts.append(f"      <target type='{vm_console_target_type}' port='{vm_console_target_port}'/>")
xml_parts.append(f"    </console>")

# Memballoon
xml_parts.append(f"    <memballoon model='{vm_memballoon_model}'/>")

xml_parts.append(f"  </devices>")

# Lifecycle Events
xml_parts.append(f"  <on_poweroff>{vm_on_poweroff}</on_poweroff>")
xml_parts.append(f"  <on_reboot>{vm_on_reboot}</on_reboot>")
xml_parts.append(f"  <on_crash>{vm_on_crash}</on_crash>")

xml_parts.append(f"</domain>")

# Print generated XML part by part
for part in xml_parts:
    print(part)
