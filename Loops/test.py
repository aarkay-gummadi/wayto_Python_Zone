while kubectl get deployment/myapp | grep -q 0/1; do
    echo "Waiting for myapp to be ready..."
    sleep 10
done
