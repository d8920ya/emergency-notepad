# Emergency Notepad di Kubernetes
---
### 1. Pastikan minikube siap digunakan untuk membangun aplikasi.
```
minikube start
kubectl cluster-info
kubectl get nodes
```
![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/1_KubernetesNodes.jpg "Pastikan Nodes sudah running")

---

### 2. Buat file rc.yaml dan deployment.yaml
Masukkan file verikut ke environment kubernetes, bisa menggunakan `vi` atau transfer menggunakan cara lain (`sftp`, `wget`, `echo`, dsb).
- [File rc.yaml untuk Replication Controller](rc.yaml)
- [File deploy.yaml untuk Deployment](deploy.yaml)

---

### 3. Mengaktifkan Replication Controller
kubectl create -f rc.yaml
kubectl describe rc notepad
kubectl expose rc notepad --port=80 --target-port=80 --type=NodePort
kubectl get service
kubectl describe service notepad

![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/2_ReplicationController-1.jpg "Dokumentasi Replication Controller #1")
![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/3_ReplicationController-2.jpg "Dokumentasi Replication Controller #2")

---

### 4. Mengaktifkan Deployment
kubectl create -f deploy.yaml
kubectl describe deployment notepad
kubectl expose deployment notepad --port=80 --target-port=80 --type=NodePort
kubectl get service
kubectl describe service notepad

![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/4_Deployment-1.jpg "Dokumentasi Deployment #1")
![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/5_Deployment-2.jpg "Dokumentasi Deployment #2")

---

### Uji Coba Aplikasi
![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/6_TestStateless-1.jpg "Menambahkan notes di pods 1")
![alt text](https://github.com/d8920ya/emergency-notepad/blob/master/Pictures/7_TestStateless-2.jpg "Menambahkan notes di pods 2")
