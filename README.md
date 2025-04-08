# Skalierung der Anwendung – Kayf.App

Dieses Repository enthält alle relevanten Komponenten zur **Skalierung der Anwendung [Kayf.App](https://kayf.app/)** im Rahmen meiner Diplomarbeit. Ziel war es, die Anwendung containerisiert bereitzustellen und sie dynamisch skalierbar zu machen.

## Projektstruktur

| Ordner            | Beschreibung                                                                 |
|-------------------|------------------------------------------------------------------------------|
| `cluster_setup/`  | Setups und Hilfstools zum Starten eines lokalen Clusters (z. B. Minikube)    |
| `deployments/`    | Helm-Charts und Kubernetes-Deployment-Konfigurationen                        |
| `Autoscaler/`     | Eigener Python-basierter Autoscaler zur dynamischen Skalierung               |

---

## Anforderungen

- [Python 3.9](https://www.python.org/downloads/)
- [Kubernetes / Minikube](https://minikube.sigs.k8s.io/)
- [Docker](https://www.docker.com/)
- [Helm 3](https://helm.sh/)

---

