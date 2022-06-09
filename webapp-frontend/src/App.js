import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import Shop from './Shop';
import Order from './Order';
import state from './catalog/state';



function App() {

  const [order, updateOrdr] = useState(state);

  window.Telegram.WebApp.onEvent('mainButtonClicked', function(e) {
    window.Telegram.WebApp.MainButton.showProgress()
    let req = new XMLHttpRequest();
  
    req.onreadystatechange = () => {
      if (req.readyState == XMLHttpRequest.DONE) {
          //send order to backend
          window.Telegram.WebApp.sendData(order)
      }
    };
  })
  
  const addProduct = (p) => {
    order[p].count = order[p].count + 1
    updateOrdr(ordr=>[...ordr]) //little hack
    if (order.map(it => it > 0).length > 0 ) {
        window.Telegram.WebApp.MainButton.isVisible = true
        window.Telegram.WebApp.MainButton.text = 'Order sum: ' + order.reduce((t, c) => t = t + c.count,0) * state[p].price +' $.' 
    }
  }
  const rmProduct = (p) => {
    order[p].count = 0
    updateOrdr(ordr=>[...ordr])
    if (order.map(it => it > 0).length > 0 ) {
        window.Telegram.WebApp.MainButton.isVisible = true
        window.Telegram.WebApp.MainButton.text = 'Order sum: ' + order.reduce((t, c) => t = t + c.count,0) * state[p].price +' $.' 
    } else {
      window.Telegram.WebApp.MainButton.isVisible = false
    }
  }

  return (
    <div className="App">
      <Shop addProduct={addProduct} rmProduct={rmProduct} products={order} />
      <Order order={order.filter(i => i.count > 0)}/>
    </div>
  );
}

export default App;
