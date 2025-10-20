import { useState } from 'react'
import './App.css'
import {OrbitProgress} from 'react-loading-indicators'

function App() {
  const [instruction,setInstruction] = useState<string>("")
  const [success,setSuccess] = useState<boolean>(false)
  const [loading,setLoading] = useState<boolean>(false)
  const [lowestObject, setLowestObject] = useState<any>(null);
  const handleAutomated = async () => {
    try{
      const apiURL =import.meta.env.API_URL || "http://localhost:5000";
      const response = await fetch(`${apiURL}/api/sendInstruction`,{
        method: 'POST',
        headers:{
          'Content-Type':'application/json',
        },
        body: JSON.stringify({
          send_type: instruction
        })
      })
      const data = await response.json();
      if (data.success === true){
        setLowestObject(data);
        console.log(`Success: Successfully logged into website, price: ${data.result.price}`);
        setSuccess(true)
      }
    }catch(error){
      console.error(`Failure`,error);
    }
  }
  return (
    <>
      <title>Welcome to AutoTasker</title>
      
      <h1>Amazon Lowest Price Finder</h1>
      <h4>Example Prompt: Enter the name of the product you want the lowest price of</h4>
      <h4>formating should be like this: [productname]_[productname-secondpart] (eg. blue_shirt)</h4>
      <input placeholder="Enter instruction" onChange={(e)=>setInstruction(e.target.value)}></input>
      <button  style={{backgroundColor: "#FF9900", color: "black"}}onClick={()=>{handleAutomated();setLoading(true)}} disabled={instruction.length===0}>do automated</button>
      {loading && <div style={{alignItems: "center",justifyContent:"center",alignContent:"center",display:"flex", marginTop: 30, padding: 10,backgroundColor:"#FF9900",borderRadius: 10}}><span style={{fontSize: 30,color:"black"}}>Loading</span> <OrbitProgress color="black" size="small" text="" textColor="" /></div>}
      {success && <div style={{border: "5px solid black", padding: 20, borderRadius: 10,marginTop: 20,backgroundColor: "#FF9900", color: "black"}}>
        <h1>Lowest Price: {lowestObject.result.price}</h1>
        <button style={{padding: 20, color: "white", backgroundColor: "black"}} onClick={()=>window.open(lowestObject.result.url)}>View Product</button>
        </div>}
    </>
  )
}

export default App
