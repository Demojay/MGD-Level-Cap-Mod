init -999 python:
    #Patch file to fix issues with ReplaceNext() Function
    # Changes the 'next' node of a node to a new target, and scans child branches of the node to do the same.
    # Also changes the new target's 'next' to the original 'next' node.
    global config, ReplaceNext

    def ReplaceNextPatched(node, newNext):
        printDebugStatements = hasattr(config, "developer") and config.console
        if printDebugStatements:
            print("\n\nSrarting Patched ReplaceNext function:")

        def ScanTree(base, old, new, subAvoid = []):
            iterNode = base
            while iterNode != None and iterNode not in subAvoid:
                if printDebugStatements:
                    if type(iterNode) == renpy.ast.Jump:
                        print("Jump node: " + iterNode.target + ", Next Node: Class" + str(iterNode.next))
                    elif type(iterNode) == renpy.ast.Python:
                        print("Python node: " + iterNode.code.source + ", Next Node Class: " + str(iterNode.next))
                    elif type(iterNode) == renpy.ast.If:
                        print("If node: " + ",".join([tupleEle[0] for tupleEle in iterNode.entries]) + " - Next Node Class: " + str(iterNode.next))
                    else:
                        print("Other node: " + str(iterNode) + " Next Node: " + str(iterNode.next))

                if type(iterNode) == renpy.ast.If:
                    for ifEntry in iterNode.entries:
                        ScanTree(ifEntry[1][0], old, new, subAvoid + [iterNode.next])
                
                if type(iterNode) == renpy.ast.Menu:
                    for menuItem in iterNode.items:
                        if menuItem[2] != None:
                            ScanTree(menuItem[2][0], old, new, subAvoid + [iterNode.next])
                
                if type(iterNode) == renpy.ast.While:
                    ScanTree(iterNode.block[0], old, new, subAvoid + [iterNode])
                
                if iterNode != node:
                    if iterNode.next == old:
                        if printDebugStatements:
                            print("Next Node replaced: " + str(iterNode.next) + " to " + str(new))
                        iterNode.next = new
                    
                
                iterNode = iterNode.next
        
        prevNext = node.next
        if type(newNext).__name__ == "list":
            node.next = newNext[0]
            if printDebugStatements:
                print("\nScanTree function call: node to newNext List Start")
            ScanTree(node, prevNext, newNext[0], [newNext[0]])
            if printDebugStatements:
                print("\nScanTree function call: newNext List End to prevNext")
            ScanTree(newNext[-1], newNext[-1].next, prevNext, [prevNext])
        else:
            node.next = newNext
            if printDebugStatements:
                print("\nScanTree function call: node to newNext")
            ScanTree(node, prevNext, newNext, [newNext])
            if printDebugStatements:
                print("\nScanTree function call: node to prevNext")
            ScanTree(newNext, newNext.next, prevNext, [prevNext])
        
        if printDebugStatements:
            print("\nEnding Patched ReplaceNext function\n\n")

    originalReplaceNext = ReplaceNext
    ReplaceNext = ReplaceNextPatched

    def FindNodePatched(baseNode, nodeType, query, exactMatch = False, subAvoid = []):
        iterNode = baseNode
        if type(subAvoid) != list:
            subAvoid = [subAvoid]

        while iterNode != None and iterNode not in subAvoid:
            if type(iterNode) == renpy.ast.Say or (Rentime_Compat_HasTranslateSay == True and type(iterNode) == renpy.ast.TranslateSay):
                if nodeType == "Say":
                    if (exactMatch == True and iterNode.what == query) or (exactMatch == False and query in iterNode.what):
                        return iterNode
                elif nodeType == "Sayer":
                    if (exactMatch == True and iterNode.who == query) or (exactMatch == False and query in iterNode.who):
                        return iterNode
            
            if nodeType == "Python" and type(iterNode) == renpy.ast.Python:
                if (exactMatch == True and iterNode.code.source == query) or (exactMatch == False and query in iterNode.code.source):
                    return iterNode
            
            if nodeType == "Jump" and type(iterNode) == renpy.ast.Jump:
                if (exactMatch == True and iterNode.target == query) or (exactMatch == False and query in iterNode.target):
                    return iterNode
            
            if nodeType == "Call" and type(iterNode) == renpy.ast.Call:
                if (exactMatch == True and iterNode.label == query) or (exactMatch == False and query in iterNode.label):
                    return iterNode
            
            if type(iterNode) == renpy.ast.If:
                for ifEntry in iterNode.entries:
                    if nodeType == "If":
                        if (exactMatch == True and ifEntry[0] == query) or (exactMatch == False and query in ifEntry[0]):
                            return iterNode
                    # Check sub-branches contained by If node
                    checkBranch = FindNode(ifEntry[1][0], nodeType, query, exactMatch, subAvoid + [iterNode.next])
                    if checkBranch is not None:
                        return checkBranch
            
            # Scan Translate blocks
            if type(iterNode) == renpy.ast.Translate:
                checkBranch = FindNode(iterNode.block[0], nodeType, query, exactMatch, subAvoid + [iterNode.next])
                if checkBranch is not None:
                    return checkBranch
            
            # Scan Menu branches
            if type(iterNode) == renpy.ast.Menu:
                for menuItem in iterNode.items:
                    if menuItem[2] is not None: # don't check menu captions
                        if nodeType == "Menu":
                            if (exactMatch == True and menuItem[0] == query) or (exactMatch == False and query in menuItem[0]):
                                return iterNode
                        # Check sub-branches contained by Menu node
                        checkBranch = FindNode(menuItem[2][0], nodeType, query, exactMatch, subAvoid + [iterNode.next])
                        if checkBranch is not None:
                            return checkBranch
            
            # Scan While nodes
            if type(iterNode) == renpy.ast.While:
                if nodeType == "While":
                    if (exactMatch == True and iterNode.condition == query) or (exactMatch == False and query in iterNode.condition):
                        return iterNode
                checkBranch = FindNode(iterNode.block[0], nodeType, query, exactMatch, subAvoid + [iterNode])
                if checkBranch is not None:
                    return checkBranch
            
            # Scan sub-labels
            if type(iterNode) == renpy.ast.Label and len(iterNode.block) > 0:
                checkBranch = FindNode(iterNode.block[0], nodeType, query, exactMatch, subAvoid + [iterNode.next])
                if checkBranch is not None:
                    return checkBranch
            
            # Scan UserStatements
            if type(iterNode) == renpy.ast.UserStatement:
                if nodeType == "Call" and iterNode.parsed[0][0] == "call":
                    if (exactMatch == True and iterNode.parsed[1]["name"] == query) or (exactMatch == False and query in iterNode.parsed[1]["name"]):
                        return iterNode
            
            # Check the next node
            iterNode = iterNode.next
        return None

    originalFindNode = FindNode
    FindNode = FindNodePatched