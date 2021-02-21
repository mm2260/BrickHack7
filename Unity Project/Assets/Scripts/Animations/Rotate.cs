using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    [SerializeField] private float rotationSpeed = 12f;
    private void Update()
    {
        transform.Rotate((Vector3.up + Vector3.right) * (float) ( rotationSpeed * Math.Sin(Time.time) * Time.deltaTime ) );
    }
}
