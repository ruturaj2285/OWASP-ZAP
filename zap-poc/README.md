# OWASP ZAP on EKS – GitHub Actions Pipeline

This repo demonstrates an **end-to-end security scan** using **OWASP ZAP** running inside an **EKS cluster**, triggered automatically from **GitHub Actions**.

---

## 🧩 Structure

| Folder | Purpose |
|---------|----------|
| `.github/workflows/` | CI workflow connecting GitHub → AWS EKS |
| `k8s/` | Kubernetes manifests for demo Flask app and ZAP |
| `src/` | Example Flask API to scan |
| `reports/` | Local copy of generated ZAP reports |
| `.gitignore` | Ignores virtual-env, caches, and reports |

---

## 🚀 Quick Usage

1. **Push** this repo to GitHub.  
2. **Create** an IAM role for GitHub OIDC with EKS access.  
3. Go to **Actions → “OWASP ZAP on EKS (End-to-End)” → Run workflow.**  
4. Input values (region, cluster, namespace, etc.).  
5. After it finishes, download the artifact: **zap-report/report.html**.

---

## 🧪 Optional: Run Manually
```bash
kubectl apply -f k8s/flask-deploy.yaml -n zap-poc
kubectl apply -f k8s/zap-pvc.yaml -n zap-poc
kubectl apply -f k8s/zap-deploy.yaml -n zap-poc
kubectl apply -f k8s/zap-service.yaml -n zap-poc

