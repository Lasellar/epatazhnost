import React from 'react';

const Slider = () => {
    return (
        <div
            id="carouselExampleIndicators"
            className="carousel slide"
            data-bs-ride="carousel"
            style={{
                display: 'flex',
                justifyContent: 'center',
                overflow: 'hidden',
            }}
        >
            <ol className="carousel-indicators" style={{
                backgroundColor: 'black'
            }}>
                <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" className="active"></li>
                <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></li>
                <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></li>
            </ol>

            <div className="carousel-inner">
                <div className="carousel-item active">
                    <img
                        src="/photoTest.svg"
                        alt="First slide"
                        className="d-block w-100"
                        style={{height: '570px', objectFit: 'contain'}}
                    />
                </div>

                <div className="carousel-item">
                    <img
                        src="/photoTest.svg"
                        alt="Second slide"
                        className="d-block w-100"
                        style={{height: '570px', objectFit: 'contain'}}
                    />
                </div>

                <div className="carousel-item">
                    <img
                        src="/photoTest.svg"
                        alt="Third slide"
                        className="d-block w-100"
                        style={{height: '570px', objectFit: 'contain'}}
                    />
                </div>
            </div>

            <button
                className="carousel-control-prev"
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="prev"
                style={{
                    width: '100px',
                    backgroundColor: 'purple',
                    border: 'none',
                }}
            >
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Previous</span>
            </button>

            <button
                className="carousel-control-next"
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="next"
                style={{
                    width: '100px',
                    backgroundColor: 'purple',
                    border: 'none',
                }}
            >
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Next</span>
            </button>
        </div>
    );
};

export default Slider;
