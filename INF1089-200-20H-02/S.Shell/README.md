# Shell

```bash
cat > get-outputs.sh << 'EOF'
#!/bin/bash
function usage {
  echo "usage: source <(./get-outputs.sh <param1> <param2>)"
  echo "param1 is for ..."
  echo "param2 is for ..."
}

function main {
    #Get Param1
    if [ -z "$1" ]; then
            echo "please provide param1"
            usage
            exit 1
    else
        myParam1="$1"
    fi
    #Get Param2
    if [ -z "$2" ]; then
            echo "please provide param2"
            usage
            exit 1
    else
        myParam2="$2"
    fi
    
    echo "#Param1: $myParam1"
    echo "#---"
    
    echo "#Param2: $myParam2"
    echo "#---"
}
main "$@"
EOF
```

```bash
#Add executable permissions
chmod +x get-outputs.sh
```
