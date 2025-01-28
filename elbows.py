# Nuke Script to create dots to organize nodegraph so that input streams are straight (B pipes or A pipes or masks)

import nuke


def create_dot(xpos, ypos):
    dot = nuke.nodes.Dot()
    dot.setXYpos(xpos, ypos)
    return dot


def check_misalignment(input_data, selected_node):
    """Check if inputs are misaligned with the selected node."""
    dot_size = int(nuke.toNode("preferences")['dot_node_scale'].value() * 12)
    
    if input_data["input"] == 0:
        # For B pipe, check if input x position matches selected node x position
        input_center_x = input_data["xpos"] + input_data["node"].screenWidth()/2
        selected_center_x = selected_node.xpos() + selected_node.screenWidth()/2
        if abs(input_center_x - selected_center_x) > 1:  # Allow 1 pixel tolerance
            input_data["misaligned"] = True
            
    elif input_data["input"] == 1:
        # For A pipe, check if input y position matches selected node y position
        input_center_y = input_data["ypos"] + input_data["node"].screenHeight()/2
        selected_center_y = selected_node.ypos() + selected_node.screenHeight()/2
        if abs(input_center_y - selected_center_y) > 1:  # Allow 1 pixel tolerance
            input_data["misaligned"] = True
            
    elif input_data["input"] == 2:
        # For mask, check if input y position matches selected node y position
        input_center_y = input_data["ypos"] + input_data["node"].screenHeight()/2
        selected_center_y = selected_node.ypos() + selected_node.screenHeight()/2
        if abs(input_center_y - selected_center_y) > 1:  # Allow 1 pixel tolerance
            input_data["misaligned"] = True


def main():
    """Main function to create elbow dots for the selected node."""
    try:
        selected_node = nuke.selectedNode()
    except ValueError:
        nuke.message("Please select a node")
        return

    # Get number of inputs
    num_inputs = selected_node.inputs()

    # Create dots for each input
    for i in range(num_inputs):
        input_node = selected_node.input(i)
        if not input_node:
            continue
            
        # Collect info on input node
        input_data = {
            "node": input_node,
            "input": i,
            "xpos": input_node.xpos(),
            "ypos": input_node.ypos(),
            "misaligned": False
        }   

        # Check for misalignment
        check_misalignment(input_data, selected_node)

        # Create dots for misaligned inputs
        if input_data["misaligned"]:
            dot_size = int(nuke.toNode("preferences")['dot_node_scale'].value() * 12)
            if input_data["input"] == 0:  # B pipe
                dot = create_dot(
                    selected_node.xpos() + selected_node.screenWidth()//2 - dot_size//2,
                    input_data["ypos"] + input_data["node"].screenHeight()//2 - dot_size//2
                )
                dot.setInput(0, input_data["node"])
                selected_node.setInput(input_data["input"], dot)
            elif input_data["input"] in [1, 2]:  # A pipe or mask
                dot = create_dot(
                    input_data["xpos"] + input_data["node"].screenWidth()//2 - dot_size//2,
                    selected_node.ypos() + selected_node.screenHeight()//2 - dot_size//2
                )
                dot.setInput(0, input_data["node"])
                selected_node.setInput(input_data["input"], dot)


if __name__ == '__main__':
    main()