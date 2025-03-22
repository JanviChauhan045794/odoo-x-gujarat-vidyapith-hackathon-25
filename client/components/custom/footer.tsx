'use client'
import { LogoLabelComp } from "@/components/custom/logo-label";
import { LinkPreview } from "@/components/ui/link-preview";
// import { assetsLinks } from "@/lib/assets-links";
import { pageLinks } from "@/lib/page-links";
import { LucideCopyright } from "lucide-react";
// import Image from "next/image";
import Link from "next/link";

/**
 * The Global Footer component
 */
export function FooterComp() {
    const menuItems = [
        {
            title: "Product",
            links: [
                { text: "Overview", url: pageLinks.nav.products },
                { text: "Pricing", url: pageLinks.nav.pricing },
                { text: "Marketplace", url: pageLinks.nav.marketplace },
                { text: "Features", url: pageLinks.nav.features },
            ],
        },
        {
            title: "Resources",
            links: [
                { text: "Community", url: "#" },
                { text: "Docs", url: "#" },
                { text: "Guides", url: "#" },
                { text: "Support", url: pageLinks.legal.support },
                { text: "Pricing", url: "#" },
            ],
        },
        {
            title: "Company",
            links: [
                { text: "About", url: pageLinks.nav.about },
                { text: "Blog", url: pageLinks.resource.blog },
                { text: "Team", url: pageLinks.resource.team },
                { text: "Careers", url: pageLinks.resource.careers },
                { text: "Contact Us", url: pageLinks.resource.contact },
                { text: "Privacy Policy", url: pageLinks.legal.privacy },
                { text: "Partners", url: pageLinks.resource.partners },
            ],
        },
        // {
        //     title: "Social",
        //     links: [
        //         { src: assetsLinks.social.github.src, alt: assetsLinks.social.github.alt, text: "Github", url: pageLinks.social.github },
        //         { src: assetsLinks.social.linkedIn.src, alt: assetsLinks.social.linkedIn.alt, text: "LinkedIn", url: pageLinks.social.linkedIn },
        //         { src: assetsLinks.social.youtube.src, alt: assetsLinks.social.youtube.alt, text: "YouTube", url: pageLinks.social.youtube },
        //         { src: assetsLinks.social.instagram.src, alt: assetsLinks.social.instagram.alt, text: "Instagram", url: pageLinks.social.instagram },
        //         { src: assetsLinks.social.twitter.src, alt: assetsLinks.social.twitter.alt, text: "Twitter", url: pageLinks.social.twitter },
        //     ],
        // },
    ]

    const bottomLinks = [
        { text: "Terms and Conditions", url: pageLinks.legal.terms },
        { text: "Privacy Policy", url: pageLinks.legal.privacy },
    ]

    return (
        <div className="container font-sans pb-8">
            <footer>
                <div className="grid grid-cols-2 gap-8 px-5 pt-5 border-t lg:grid-cols-6 border-border/20">
                    <div className="col-span-2 mb-8 lg:mb-0">
                        <div className="flex items-center gap-2 lg:justify-start">
                            <Link href={pageLinks.nav.home} className="flex items-center">
                                {/* <Image
                                    src={assetsLinks.fraxation_logo.src}
                                    alt={assetsLinks.fraxation_logo.alt}
                                    title={"Fraxation Logo"}
                                    width={80}
                                    height={80}
                                /> */}
                                <LogoLabelComp className="text-3xl" />
                            </Link>
                        </div>
                        <blockquote className="pl-6 mt-6 italic border-l-2">
                            &quot;Let AI Handle Setup, You Handle Innovation.&quot;
                        </blockquote>
                    </div>
                    {menuItems.map((section, sectionIdx) => (
                        <div key={sectionIdx}>
                            <h3 className="mb-4 font-bold">{section.title}</h3>
                            <ul className="space-y-4 text-neutral-300/50 text-sm">
                                {section.links.map((link, linkIdx) => (
                                    <div key={linkIdx}>
                                        {"src" in link ?
                                            (
                                                <div className="flex items-center space-x-1 hover:text-white group">
                                                    {/* <Image src={link.src} alt={link.alt} width={20} height={20} className="bg-lime-300/50 group-hover:bg-lime-300 rounded-xs" /> */}
                                                    <LinkPreview
                                                        width={300}
                                                        height={200}
                                                        url={link.url}
                                                        className="hover:text-foreground text-neutral-300/50"
                                                    >
                                                        {link.text}
                                                    </LinkPreview>
                                                </div>
                                            ) : (
                                                <a href={link.url} className="flex items-center space-x-1 hover:text-white group">
                                                    <li>
                                                        {link.text}
                                                    </li>
                                                </a>
                                            )
                                        }
                                    </div>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
                <div className="flex flex-col justify-between gap-4 px-5 pt-8 mt-24 text-sm font-medium border-t border-border/10 text-foreground md:flex-row md:items-center">
                    <div className="flex items-center space-x-1">
                        <LucideCopyright size={12} />
                        <span>2025 Copyright. All rights reserved.</span>
                    </div>
                    <ul className="flex gap-4">
                        {bottomLinks.map((link, linkIdx) => (
                            <li key={linkIdx} className="underline hover:text-foreground">
                                <a href={link.url}>{link.text}</a>
                            </li>
                        ))}
                    </ul>
                </div>
            </footer >
        </div >
    );
};
