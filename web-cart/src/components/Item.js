import React, {Component} from 'react'

class Item extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="card" style={{width: '400px'}}>
                <div className="card-header">
                    {this.props.item.title}
                    <button onClick={(index)=>this.props.deleteItemFunc(this.props.index)} className="btn btn-primary btn-lg float-right">Удалить товар</button>
                </div>
                <div className="card-body float-right">{this.props.item.cost} Руб.</div>
            </div>
        )
    }
}

export default Item