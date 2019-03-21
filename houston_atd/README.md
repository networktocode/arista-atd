# Arista ATD: Houston 12/06/2018

## Overview

The purpose of this project is two fold:

1. One-Click provision of a VXLAN/EVPN enabled Arista data center [one-click provision playbook](./vxlan_provision.yml)
2. Add additional VLANs to the EVPN fabric [add vlans to evpn playbook](./vxlan_add_vlan.yml) 

### Topology 

- eBGP used both within the underlay and overlay
- iBGP between MLAG peers
- Hosts are dual connected
  - Host 1 in Vlan13
  - Host 2 in Vlan12
  - Host 3 in Vlan13
  - Host 4 in Vlan12

### Goal

We are looking for Layer2 reachability across VXLAN/EVPN fabric

#### topology overview

![alt text](documentation/data_center.jpg)
