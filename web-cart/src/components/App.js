import React, {Component} from 'react';
import ItemList from "./ItemList";
import CostView from "./CostView";
import items from "../items";
import 'bootstrap/dist/css/bootstrap.css'

class App extends Component{

    constructor(props) {
        super(props);

        this.state = {
            finalCost : 0,
            items : items,
            isBuy : false
        };

        this.deleteItem = this.deleteItem.bind(this);
        this.handleBuy = this.handleBuy.bind(this);

        this.calculateFinalCost();
    }

    deleteItem(index){
        console.log('---', 'deleted:', index)
        this.state.items.splice(index, 1);
        this.calculateFinalCost();
        this.setState(this.state);
    }

    calculateFinalCost(){
        let final_cost = 0;

        for (let i = 0; i < this.state.items.length; i++)
        {
            final_cost += this.state.items[i].cost
        }

        this.state.finalCost = final_cost;
        this.setState(this.state);
    }

    handleBuy(){
        this.setState({isBuy : true, finalCost : 0});
    }

    render() {
        let isEmpty = <div className="container">
            <h3 className="jumbotron">Корзина покупок</h3>
            <div>
                <div className="float-left">Корзина пуста!</div>
                <CostView finalCost = {this.state.finalCost} buyHandle = {this.handleBuy}/>
            </div>
        </div>;
        let noEmpty =
            <div className="container">
                <h3 className="jumbotron">Корзина покупок</h3>
                <div>
                    <ItemList deleteItemFunc = {this.deleteItem} items={items}/>
                    <CostView finalCost = {this.state.finalCost} buyHandle = {this.handleBuy}/>
                </div>
            </div>;
        let body = this.state.isBuy ? isEmpty : noEmpty;

        return (
            <div>
                {body}
            </div>
        )
    }
}

export default App;
