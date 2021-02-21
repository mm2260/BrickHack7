using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class PlacementIndicator : MonoBehaviour
{

    private ARRaycastManager _raycastManager;
    private GameObject _indicatorGameObject;

    [SerializeField] private float movementVelocity = 2f;
    
    // Start is called before the first frame update
    void Start()
    {
        _raycastManager = FindObjectOfType<ARRaycastManager>();
        _indicatorGameObject = transform.GetChild(0).gameObject;
        
    }

    // Update is called once per frame
    void Update()
    {

        var raycastHits = new List<ARRaycastHit>();
        _raycastManager.Raycast(
            new Vector2(Screen.width / 2f,
                                  Screen.height / 2f),
            raycastHits,
            TrackableType.Planes );

        if (raycastHits.Count > 0)
        {
            var t = transform;
            t.position = Vector3.Lerp(t.position, raycastHits[0].pose.position, Time.deltaTime*movementVelocity ); ;
            t.rotation = raycastHits[0].pose.rotation;
        }
        
    }
}
