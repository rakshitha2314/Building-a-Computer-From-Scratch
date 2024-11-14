for i in range(2**7):
    #print(i)
    inp = bin(i)[2:]
    n = len(inp)
    for count in range (7-n):
        inp = "0" + inp
    #print(inp)
    OPcode = inp[2:]
    #print(OPcode)
    Imm = inp[1]
    
    IsEq = inp[0]

    #op-code reading
    add = 0
    if (OPcode == "00000"):
        add = 1

    sub = 0
    if (OPcode == "00001"):
        sub = 1

    cmp = 0
    if (OPcode == "00101"):
        cmp = 1

    ld = 0
    if (OPcode == "01110"):    
        ld = 1

    st = 0
    if (OPcode == "01111"):
        st = 1

    beq = 0
    if (OPcode == "10000"):
        beq = 1

    call = 0
    if (OPcode == "10011"):
        call = 1

    ret = 0
    if (OPcode == "10100"):
        ret = 1

    halt = 0
    if (OPcode == "11111"):
        halt = 1

    #combinatorial cicuit encoding
    alu_sel = "0000"
    if (sub):
        alu_sel = "0001"

    regwen = str(int(add or ld or sub))

    flwen = str(int(cmp))

    bsel = str(int(Imm))

    wbsel = str(int(ld))

    rs2rdsel = str(int(st))

    wra = str(int(call))

    retpc = str(int(ret))

    hsel = str(0)
    if (halt == 0):
        hsel = str(1)

    branchbeq = str(int(IsEq and beq))

    pcsel = str(int(branchbeq or call))

    out = regwen+bsel+flwen+alu_sel+wbsel+rs2rdsel+pcsel+wra+retpc+hsel
    out_str = hex(int(out,2))[2:]
    m = len(out_str)
    for count in range(4-m):
        out_str = "0" + out_str
    print (out_str, end=" ")
    if ((i+1)%8==0):
        print()
        