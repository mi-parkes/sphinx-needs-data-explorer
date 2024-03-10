function startTimer() {
    startTime = performance.now();
}

function stopTimer(msg) {
    const endTime = performance.now();
    console.log(`Execution time of ${msg}`,endTime - startTime);
}

class Node {
    constructor(left, right, operand) {
    this.left = left;
    this.right = right;
    this.operand = operand;
    };
    static class(obj) {
        return new Node(obj.left,obj.right,obj.operand);
    }
    get(node) {
        return Node.create(node).expand();
    }
    getValue(node) {
        // console.log('expand():',this);
        if('type' in node) {
            if(node['type']=='array')
                return node.value;
            else
                return node.value;
        } else 
            return this.get(node)
    }
    expand() {
        //console.log('expand():',this);
        //console.log('typeof this.left',typeof this.left);
        //console.log('typeof this.right',typeof this.right);
        let lhs='type' in this.left ?
            this.getValue(this.left):this.get(this.left);
        let rhs='type' in this.right ? 
            this.getValue(this.right):this.get(this.right);
        return `${lhs} ${this.operand} ${rhs}`
    }
    print() {
        console.log(this.expand());
    }
    cast(node) {
        return Node.create(node);
    }
    //isObject(node) { return typeof node === "object" }
    isObject(node) { return !('type' in node); }
    evaluate(currentNode) {
        var ret=false;
        // console.log(`" --> ${this.operand}"`);
        switch (this.operand) {
            //  '..' in attr
            case "in_1":
                ret=(this.right['value'] in currentNode['data']) && 
                    currentNode['data'][this.right['value']].includes(this.left['value']);
                // console.log(`${this.left} in ${this.right} = ${ret}`);
                break;                
            // attr in ['..','..']
            case "in_3":
                ret=(this.left['value'] in currentNode['data']) && 
                    this.right['value'].split(",").includes(currentNode['data'][this.left['value']]);
                break;
            // ['..','..'] in attr
            case "in_4":
                ret=(this.right['value'] in currentNode['data']) && 
                    this.left['value'].split(",").some(v=> currentNode['data'][this.right['value']].includes(v))
                break;
            // '..' == attr 
            case "==1":
                ret=(this.right['value'] in currentNode['data']) && 
                (currentNode['data'][this.right['value']]==this.left['value']);
                break;
            // attr == '..'
            case "==2":
                ret=(this.left['value'] in currentNode['data']) && 
                (currentNode['data'][this.left['value']]==this.right['value']);
                break;
            // attr == []
            case "==3":
                ret=false;
                var lhs=null;
                if(this.left['value']==='outgoing') {
                    if('attr' in this.left) {
                        //console.log('parents',this.left['attr'])
                        lhs=parents[currentNode['data']['id']]
                    } else
                        lhs=parents[currentNode['data']['id']]
                }
                else
                if(this.left['value']==='incoming') {
                    if('attr' in this.left) {
                        //console.log('children',this.left['attr'])
                        lhs=children[currentNode['data']['id']]
                    } else
                        lhs=children[currentNode['data']['id']]
                }
                else
                    if(this.left['value'] in currentNode['data'])
                        lhs=currentNode['data'][this.left['value']]
                if(lhs!=null) {
                    if((this.right['value']==='')) {
                        ret=lhs.length===0;
                        //console.log(currentNode['data']['id']);
                    } else {
                        //console.log(currentNode['data']['id']);
                        ret=false;
                        //ret=lhs===this.right['value']
                    }
                }
                break;
            // attr != []
            case "==4":
                ret=false;
                var lhs=null;
                if(this.left['value']==='outgoing')
                    lhs=parents[currentNode['data']['id']]
                else
                if(this.left['value']==='incoming')
                    lhs=children[currentNode['data']['id']]
                else
                    if(this.left['value'] in currentNode['data'])
                        lhs=currentNode['data'][this.left['value']]
                if(lhs!=null) {
                    if((this.right['value']==='')) {
                        ret=lhs.length>0;
                        //console.log(currentNode['data']['id']);
                    } else {
                        //console.log(currentNode['data']['id']);
                        ret=false;
                    }
                }
                break;
            // attr != '..'
            case "==5":
                ret=(this.left['value'] in currentNode['data']) && 
                (currentNode['data'][this.left['value']]!==this.right['value']);
                break;
            case "&&":
                ret=(
                (this.isObject(this.left) ? this.cast(this.left).evaluate(currentNode)   : this.left['value']) && 
                (this.isObject(this.right) ? this.cast(this.right).evaluate(currentNode) : this.right['value'])
                )
                //console.log(`${this.left} in ${this.right} = ${ret}`);
            break;
            case "||":
                ret=(
                    (this.isObject(this.left)  ? this.cast(this.left).evaluate(currentNode)  : this.left['value']) ||
                    (this.isObject(this.right) ? this.cast(this.right).evaluate(currentNode) : this.right['value'])
                    )
                break;
            case "()":
                ret=(this.isObject(this.right) ? this.cast(this.right).evaluate(currentNode) : this.right['value']);
                break;
            case "()||":
                ret=(this.isObject(this.left) ? this.cast(this.left).evaluate(currentNode)   : this.left['value']) ||
                    (this.isObject(this.right) ? this.cast(this.right).evaluate(currentNode) : this.right['value']);
                break;
            case "()&&":
                ret=(this.isObject(this.left)  ? this.cast(this.left).evaluate(currentNode)  : this.left['value']) &&
                    (this.isObject(this.right) ? this.cast(this.right).evaluate(currentNode) : this.right['value']);
                break;
            case "EOL":
                ret=true;
                break;
            case "~":
                //console.log(`${this.left} in ${this.right} = ${ret}`);
                // var re = new RegExp("a|b", "i");
                var re = new RegExp(this.right['value']);
                ret=(this.left['value'] in currentNode['data']) && 
                (currentNode['data'][this.left['value']].match(re));
                if(ret) {
                    //console.log(currentNode['data'][this.left]);
                }
                break;
            case "~i":
                //console.log(`${this.left} in ${this.right} = ${ret}`);
                // var re = new RegExp("a|b", "i");
                var re = new RegExp(this.right['value'],'i');
                ret=(this.left['value'] in currentNode['data']) && 
                (currentNode['data'][this.left['value']].match(re));
                if(ret) {
                    //console.log(currentNode['data'][this.left]);
                }
                break;
            default:
                break;
        }
        return ret;
    }
}

Node.create = function (obj) {
    var field = new Node();
    for (var prop in obj) {
        if (field.hasOwnProperty(prop)) {
            field[prop] = obj[prop];
        }
    }
    return field;
}

function convert_text_to_html(text) {
    //Escape special characters to prevent XSS attacks
    escaped_text = encodeURIComponent(text);
    html_text = escaped_text.replace('\n','<br>');
    return html_text;
}

function prepareParser() {
    const firstKey = Object.keys(gnodes)[0];
    console.log(gnodes[firstKey]['data']);
    grammar = `
        start = expr
        ws = ws:[ \t]* { return ws.join("").length>0?" ":""}
        newline = [ \\t\\n\\r]* { return { left: "", right: "", operand: "EOL" } }
        QuotedString = "'" text:[A-Za-z0-9_/\\-]* "'" { 
            return {'value':text.join(""),'location':location(),'type':'qs'};
        }

        QuotedStringx = "'" text:[A-Za-z0-9_/\\-]+ "'" { return text.join(""); }

        LOperator = "&&" / "||"

        expr =  exprz0 / expr0 / exprz2 / exprz1

        exprz1="(" ws r:expr ws ")" {
            return { left: {'value':'','type':'empty'}, right: r, operand: "()" }
        }
        
        exprz2="(" ws l:expr ws ")" ws o:LOperator ws r:expr {
            return { left:l, right: r, operand: "()"+o }
        }

        exprz0= l:expr0 ws o:LOperator ws r:expr {
            return { left: l, right: r, operand: o }
        }

        expr0 =  expr1 / expr2 / expr3 / reg_expr

        expr3 = q:QuotedString ws "in" ws w:Words {
            return { left: q, right: w, operand: 'in_1' }
        }

        //str_array="[" ws l:listElm ws "]" {return l}
        
        str_array="[" ws l:listElm ws "]" {
            return {'value':l,'location':location(),'type':'array'};
        }
        
        //return {'key':key,'location':location()};
        expr1_1 = w:Words ws "in" ws l:str_array {
            return { left: w, right: l, operand: 'in_3' }
        }

        expr1_2 = l:str_array ws "in" ws w:Words {
            return { left: l, right: w, operand: 'in_4' }
        }
        
        expr1 = expr1_1 / expr1_2

        listElm1=q:QuotedStringx ws c:"," ws l:listElm0 { return q+c+l }
        listElm0 = listElm1 / QuotedStringx
        listElm = listElm0 / ""

        expr2_1 = w:Words ws "==" ws q:QuotedString {
            return { left:w, right: q, operand: '==2' }
        }
        expr2_2 = q:QuotedString ws "==" ws w:Words {
            return { left:q, right:w, operand: '==1' }
        }
        expr2_3 = w:Words ws "==" ws a:str_array {
            return { left:w, right:a, operand: '==3' }
        }
        expr2_4 = w:Words ws "!=" ws a:str_array {
            return { left:w, right:a, operand: '==4' }
        }
        expr2_5 = w:Words ws "!=" ws q:QuotedString {
            return { left:w, right: q, operand: '==5' }
        }

        expr2 = expr2_1 / expr2_2 / expr2_3 / expr2_4 / expr2_5

        reg_expr_pattern = [^/]
        reg_expr_value=r:$(reg_expr_pattern+) {  
            return {'value':r,'location':location(),'type':'re'};
        }
        
        //reg_expr = reg_expr_cs / reg_expr_ci
        case = "i" / ""
        reg_expr = w:Words ws "~" ws "/" p:reg_expr_value "/" c:case {
            return { left:w, right:p, operand: '~'+c }
        }

        Words
            = key:$(Letter+) {
                    var keys=Object.keys(gnodes);
                    if(key.length<=30) {
                        if(keys.length==0)
                            error("No needs data available");

                        const regex = /^(incoming|outgoing)\.([A-Z_a-z]+)$/;
                        const match = regex.exec(key);
                        if(match) {
                            const ref = match[1];
                            const attr = match[2];
                            if(attr in gnodes[keys[0]]['data']) {
                                return {
                                    'value':ref,
                                    'location':location(),
                                    'type':'need-attr',
                                    'attr':attr
                                };
                            }
                        }
                        if((key==='outgoing') || (key==='incoming') || key in gnodes[keys[0]]['data']) {
                            return {'value':key,'location':location(),'type':'need-attr'};
                        }
                        else
                            error("Attribute not found in needs:"+key);
                    } else
                        error("Word does have more than 10 letters");
            }
    
        Letter=[A-Za-z_\.] //{return text.join("")}
    `;
    parser=peg.generate(grammar,traceParser?{trace:true}:{});
}

function parse_input(parser,gnodes,input) {
    var msg;
    try {
        console.log(`Parsing input !${input}!`);
        msg = parser.parse(input,{gnodes});
        console.log(`Success parsing input: ${input} parsed as ${Node.create(msg).expand()}`);
    } catch (error) {
        console.log(`Failure parsing input=${msg} ${error}`);
        msg=null;
    }
    return msg;
}

function custom_filter(key,currentNode,expr) {
    return Node.create(expr).evaluate(currentNode);
}

function test1(parser,gnodes) {
    var msg;
    const i=0;
    var testInput = [
        "'S_' in id",
        "('S_' in id)&&('3' in id)",
        "('S_' in id)&&('3' in id)",
        "'arch' in docname",
        "'architecture/architecture-needs'==docname",

        "'arch' in docname",
        "status in ['open']",
        "status in ['open','closed']",
        "status in ['abc','def','ghi']",
        "(status in ['abc'])",
        "status in ['abc'] && (status in ['abc'])",

        "status in ['abc'] && (status in ['abc']) || 'arch' in docname",
        "(status in ['abc'] && (status in ['abc'])) || 'arch' in docname",
        "(status in ['abc'] && (status in ['abc'])) || ('arch' in docname)",
        "((status in ['abc'] && (status in ['abc'])) || 'arch' in docname)",
        "(status in ['abc'])",
        "status in ['abc']",
        "(status in ['abc']) || status in ['abc']",
        "docname=='architecture/architecture-needs'",
        "status in ['open','closed']"
    ];
    testInput.forEach(function (input, i) {
        try {
            console.log(`Parsing input ${i}:!${input}!`);
            msg=parse_input(parser,gnodes,input);
            console.log(`Success parsing input: ${input} parsed as ${Node.create(msg).expand()}`);
        } catch (error) {
            console.log(`Failure parsing input=${msg} ${error}`);
            msg=null;
        }
    });
    return msg;
}
