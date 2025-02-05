import React from 'react';
import Slider from '../../components/Slider/Slider'
import MainPageStyles from './MainPage.module.scss'

const members = [
    {name: 'Влад Чернеций', role: 'вокал', imageSrc: '/path/to/image1.jpg'},
    {name: 'Макс Полушин', role: 'гитара', imageSrc: '/path/to/image2.jpg'},
    {name: 'Ален Меликсетов', role: 'бас', imageSrc: '/path/to/image3.jpg'},
    {name: 'Кирилл Анашкин', role: 'гитара', imageSrc: '/path/to/image4.jpg'},
    {name: 'Саша Гояров', role: 'барабаны', imageSrc: '/path/to/image5.jpg'}
];

const icons = [
    {src: './yand.svg', name: 'yandex'},
    {src: './apl.svg', name: 'apple'},
    {src: './sptfy.svg', name: 'spotify'},
    {src: './vkMus.svg', name: 'vkMusic'},
]

const MemberCard = ({name, role, imageSrc}: { name: string, role: string, imageSrc: string }) => (
    <div className={MainPageStyles.members}>
        <div className={MainPageStyles.border}>
            <div className={MainPageStyles.membersPhoto}></div>
        </div>
        <p>{name}</p>
        <p className={MainPageStyles.role}>{role}</p>
    </div>
);

const IconCard = ({src, name}: { src: string, name: string }) => (
    <div className={MainPageStyles.icon}>
        <img src={src} alt={name}/>
    </div>
);

const MainPage = () => {
    return (
        <div>
            <Slider/>
            <div className={MainPageStyles.wrapper}>
                <div>
                    <img src="/mainTitle.svg" alt="epatazhnost"/>
                </div>

                <div className={MainPageStyles.membersWrapper}>
                    <div className={MainPageStyles.row}>
                        {members.slice(0, 3).map((member, index) => (
                            <MemberCard key={index} {...member} />
                        ))}
                    </div>
                    <div className={MainPageStyles.row}>
                        {members.slice(3).map((member, index) => (
                            <MemberCard key={index} {...member} />
                        ))}
                    </div>
                </div>
            </div>
            <div className={MainPageStyles.footer}>
                <div className={MainPageStyles.iconsList}>
                    {icons.map((icon, index) => (
                        <IconCard key={index} {...icon}/>
                    ))}
                </div>

                <div className={MainPageStyles.description}>
                    <p className={MainPageStyles.descriptionItem}>По поводу сотрудничества писать на почту</p>
                    <p className={MainPageStyles.descriptionItem}>epatazhnost@yandex.ru</p>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
