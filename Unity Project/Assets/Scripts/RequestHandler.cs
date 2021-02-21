using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using SimpleJSON;

public class RequestHandler : MonoBehaviour
{
    private readonly string _baseURL = "35.221.21.51/";

    IEnumerator GetDataAtID(int bookID)
    {
        string requestURL = _baseURL + "/books/" + bookID.ToString();
        
        UnityWebRequest bookDataRequest = UnityWebRequest.Get(requestURL);

        yield return bookDataRequest.SendWebRequest();

        if (bookDataRequest.isNetworkError || bookDataRequest.isHttpError)
        {
            Debug.LogError(bookDataRequest.error);
            yield break;
        }

        JSONNode bookData = JSON.Parse(bookDataRequest.downloadHandler.text);
        
        
    }
}
