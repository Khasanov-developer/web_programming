import React, {Component} from "react";

class CostView extends Component{
    constructor(props) {
        super(props);
    }

    render(){
        return(
        <div className="card float-right" style={{width: '30%'}}>
            <h2 className="card-title">Итого {this.props.finalCost} Рублей</h2>
            <div className="card-body">
                <button onClick={this.props.buyHandle} className="btn btn-primary btn-lg badge-light">Купить</button>
            </div>
        </div>
    )}
}{

}

export default CostView