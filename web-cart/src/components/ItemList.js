import React, {Component} from "react";
import Item from "./Item"
import './styles.css'

class ItemList extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        const itemElements = this.props.items.map((item, index) =>
            <li key={item.id} className="item-list__li"><Item deleteItemFunc = {this.props.deleteItemFunc} index={index} item = {item}/></li>);
        return(
            <div className="float-left">
                <ul>
                    {itemElements}
                </ul>
            </div>

        )
    }
}

export default ItemList;