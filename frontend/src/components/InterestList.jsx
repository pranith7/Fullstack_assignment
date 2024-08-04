import React, { useEffect, useState } from 'react';
import axios from 'axios';

const InterestList = () => {
    const [interests, setInterests] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/interests/')
            .then(response => setInterests(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Interests</h2>
            <ul>
                {interests.map(interest => (
                    <li key={interest.id}>
                        {interest.sender} sent interest to {interest.receiver}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default InterestList;